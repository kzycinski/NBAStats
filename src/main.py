import datetime
import curses
import json
import requests
from pprint import pprint
import matplotlib.pyplot as plt

from ServerConnection import ServerConnection
from DailyScores import DailyScores

from NoDataFoundError import NoDataFoundError

server_name = "http://data.nba.net/data/10s/prod/v1"
today_date = datetime.date.today()
date = None
cursor_x = 0
cursor_y = 0
height, width = 0, 0


def print_title(start_y, start_x, title):
    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    stdscr.addstr(start_y, start_x, title)

    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)


def print_middle(msg):
    curses.start_color()
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    stdscr.clear()
    height, width = stdscr.getmaxyx()
    start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
    start_y = int((height // 2) - 2)
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(start_y, start_x, msg)


def print_info():
    cursor_x = 0
    cursor_y = 0

    curses.start_color()
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    stdscr.clear()
    height, width = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.refresh()
    title = "NBAStats"
    subtitle = "Written by Krystian Życiński"
    press = "Press any key to continue"

    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
    start_x_press = int((width // 2) - (len(press) // 2) - len(press) % 2)

    start_y = int((height // 2) - 2)

    print_title(start_y, start_x_title, title)

    stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
    stdscr.addstr(start_y + 3, start_x_press, press)

    stdscr.move(cursor_y, cursor_x)

    stdscr.refresh()

    stdscr.getch()


def game_scores():
    if date is None:
        set_data()
    try:
        daily_scores = DailyScores(server)
        daily_scores.show(daily_scores.get_scores())
    except NoDataFoundError:
        msg = "No scores information on given date, change date and try again"
        print_middle(msg)
        stdscr.getch()
    except ConnectionError:
        msg = "Cannot connect to the server"
        print_middle(msg)
        stdscr.getch()



def standings():
    if date is None:
        set_data()


def compare_players():
    if date is None:
        set_data()


def set_data():
    while True:
        while True:
            curses.start_color()
            curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

            stdscr.clear()
            height, width = stdscr.getmaxyx()

            stdscr.clear()
            stdscr.refresh()
            msg = "Enter year:"
            start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
            start_y = int((height // 2) - 2)
            stdscr.addstr(start_y, start_x, msg)

            tmp = stdscr.getstr(start_y, start_x + len(msg), 4)
            try:
                year = int(tmp.decode("utf-8"))
            except ValueError:
                msg = "Please enter valid year"
                print_middle(msg)
                stdscr.getch()
                continue
            if year < 2000 or year > today_date.year:
                msg = "Wrong year :("
                print_middle(msg)
                stdscr.getch()
                continue
            break

        while True:
            msg = "Enter month:"
            start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
            start_y = int((height // 2) - 2)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(start_y, start_x, msg)

            tmp = stdscr.getstr(start_y, start_x + len(msg), 2)
            try:
                month = int(tmp.decode("utf-8"))
            except ValueError:
                msg = "Please enter valid month"
                print_middle(msg)
                stdscr.getch()
                continue
            if month <= 0 or month > 12:
                msg = "Wrong month :("
                print_middle(msg)
                stdscr.getch()
                continue
            break

        while True:
            msg = "Enter day:"
            start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
            start_y = int((height // 2) - 2)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(start_y, start_x, msg)

            tmp = stdscr.getstr(start_y, start_x + len(msg), 4)
            try:
                day = int(tmp.decode("utf-8"))
            except ValueError:
                msg = "Please enter valid day"
                print_middle(msg)
                stdscr.getch()
                continue

            if day <= 0 or day > 31:
                msg = "Wrong day :("
                print_middle(msg)
                stdscr.getch()
                continue
            break

        try:
            global date
            date = datetime.date(year, month, day)
            global server
            server = ServerConnection(server_name, date)
        except ValueError:
            msg = "Wrong date, please check and try again :("
            print_middle(msg)
            stdscr.getch()
            continue
        break




def wrong_oprion():
    msg = "Wrong option ):"
    print_middle(msg)
    stdscr.getch()


def switcher(option):
    if option == '1':
        game_scores()
    elif option == '2':
        standings()
    elif option == '3':
        compare_players()
    elif option == '4':
        set_data()
    elif option == '5':
        exit(0)
    else:
        wrong_oprion()


def main_menu():
    while True:

        stdscr.clear()
        stdscr.refresh()

        title = "MAIN MENU"
        scores = "1. Game scores"
        standings_ = "2. Standings"
        compare = "3. Compare players"
        change = "4. Change date"
        exit_ = "5. Exit"
        enter_message = "Enter your choice: "

        stdscr.clear()
        stdscr.refresh()

        to_print = []
        to_print.extend((scores, standings_, compare, change, exit_, enter_message))

        start_x = 5

        start_y = 2

        print_title(start_y, start_x, title)

        for item in to_print:
            start_y += 2
            stdscr.addstr(start_y, start_x, item)

        curses.echo()

        stdscr.move(start_y, start_x + len(enter_message))

        tmp = stdscr.getstr(start_y, start_x + len(enter_message), 1)

        option = tmp.decode("utf-8")

        switcher(option)


def main():
    global stdscr
    stdscr = curses.initscr()
    height, width = stdscr.getmaxyx()

    curses.start_color()
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    print_info()
    main_menu()

    stdscr.clear()
    stdscr.refresh()


if __name__ == '__main__':
    main()

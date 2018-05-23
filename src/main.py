import datetime
import curses
import signal

from ServerConnection import ServerConnection
from DailyScores import DailyScores
from PlayersManagement import PlayersManagement
from NoDataFoundError import NoDataFoundError
from Standings import Standings

server_name = "http://data.nba.net/data/10s/prod/v1"
today_date = datetime.date.today()
date = None


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


def signal_handler():
    stdscr.clear()
    stdscr.refresh()
    exit(0)


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
    global standings_buff
    if date is None:
        set_data()
    while True:
        stdscr.clear()
        stdscr.refresh()

        title = "STANDINGS"
        all_st = "1. All standings"
        western = "2. Western conference standings"
        eastern = "3. Eastern conference standings"
        back = "4. Back"
        enter_message = "Enter your choice: "

        stdscr.clear()
        stdscr.refresh()

        to_print = []
        to_print.extend((all_st, western, eastern, back, enter_message))

        start_x = 5

        start_y = 2

        print_title(start_y, start_x, title)

        for item in to_print:
            start_y += 2
            stdscr.addstr(start_y, start_x, item)

        curses.echo()

        stdscr.move(start_y, start_x + len(enter_message))

        tmp = stdscr.getstr(start_y, start_x + len(enter_message), 1)

        option = int(tmp.decode("utf-8"))

        if option == 4:
            return
        elif option != 3 and option != 2 and option != 1:
            wrong_oprion()
            continue
        try:
            standings_var = Standings(server)
            if option == 1:
                standings_buff = standings_var.get_all_standings()
            elif option == 2:
                standings_buff = standings_var.get_western_standings()
            elif option == 3:
                standings_buff = standings_var.get_eastern_standings()

            standings_var.show(standings_buff)
            break
        except NoDataFoundError:
            msg = "No standings information on given date, please change date and try again."
            print_middle(msg)
            stdscr.getch()
        except ConnectionError:
            msg = "Cannot connect to the server"
            print_middle(msg)
            stdscr.getch()
        return


def compare_players():
    global mode
    if date is None:
        set_data()

    while True:
        stdscr.clear()
        stdscr.refresh()

        title = "COMPARE PLAYERS"
        season = "1. Compare season stats"
        career = "2. Compare career stats"
        back = "3. Back"
        enter_message = "Enter your choice: "

        stdscr.clear()
        stdscr.refresh()

        to_print = []
        to_print.extend((season, career, back, enter_message))

        start_x = 5

        start_y = 2

        print_title(start_y, start_x, title)

        for item in to_print:
            start_y += 2
            stdscr.addstr(start_y, start_x, item)

        curses.echo()

        stdscr.move(start_y, start_x + len(enter_message))

        tmp = stdscr.getstr(start_y, start_x + len(enter_message), 1)

        option = int(tmp.decode("utf-8"))

        if option == 3:
            return
        elif option != 2 and option != 1:
            wrong_oprion()
            continue

        curses.start_color()
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.clear()
        stdscr.refresh()
        msg = "Enter player 1 first name:"
        start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
        start_y = int((height // 2) - 2)
        stdscr.addstr(start_y, start_x, msg)

        tmp = stdscr.getstr(start_y, start_x + len(msg), 20)
        name_1 = tmp.decode("utf-8")

        stdscr.clear()
        stdscr.refresh()
        msg = "Enter player 1 last name:"
        start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
        start_y = int((height // 2) - 2)
        stdscr.addstr(start_y, start_x, msg)

        tmp = stdscr.getstr(start_y, start_x + len(msg), 20)
        surname_1 = tmp.decode("utf-8")

        stdscr.clear()
        stdscr.refresh()
        msg = "Enter player 2 first name:"
        start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
        start_y = int((height // 2) - 2)
        stdscr.addstr(start_y, start_x, msg)

        tmp = stdscr.getstr(start_y, start_x + len(msg), 20)
        name_2 = tmp.decode("utf-8")

        stdscr.clear()
        stdscr.refresh()
        msg = "Enter player 2 last name:"
        start_x = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
        start_y = int((height // 2) - 2)
        stdscr.addstr(start_y, start_x, msg)

        tmp = stdscr.getstr(start_y, start_x + len(msg), 20)
        surname_2 = tmp.decode("utf-8")

        if option == 1:
            mode = 'latest'
        elif option == 2:
            mode = 'careerSummary'

        try:
            players_mgmt = PlayersManagement(server)
            player_1 = players_mgmt.get_player(name_1, surname_1, mode).get_stats()
            player_2 = players_mgmt.get_player(name_2, surname_2, mode).get_stats()
            PlayersManagement.show(player_1 + player_2)
            break
        except NoDataFoundError:
            msg = "No scores information on name and data, please change data and try again."
            print_middle(msg)
            stdscr.getch()
        except ConnectionError:
            msg = "Cannot connect to the server"
            print_middle(msg)
            stdscr.getch()


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

        stdscr.clear()
        stdscr.refresh()
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
    signal.signal(signal.SIGINT, signal_handler)
    global stdscr

    stdscr = curses.initscr()

    curses.start_color()
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    print_info()
    main_menu()

    stdscr.clear()
    stdscr.refresh()
    """
    xd = datetime.date(2017,12,12)
    xdd = ServerConnection(server_name, xd)
    mode = 'latest'
    try:
        players_mgmt = PlayersManagement(xdd)
        #player_1 = players_mgmt.get_player(name_1, surname_1, mode)
        player_1 = players_mgmt.get_player("Kevin", "Durant", mode).get_stats()
        player_2 = players_mgmt.get_player("Russell", "Westbrook", mode).get_stats()
        pprint(player_2)

        #player_2 = players_mgmt.get_player(name_2, surname_2, mode)
        players_mgmt.show(player_1+player_2)

    except NoDataFoundError:
        msg = "No scores information on name and data, please change data and try again."
        print("xd")
    except ConnectionError:
        msg = "Cannot connect to the server"
        print("xdd")"""


if __name__ == '__main__':
    main()

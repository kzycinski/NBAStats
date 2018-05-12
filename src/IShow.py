from abc import ABCMeta, abstractmethod

class IShow:
    __metaclass__ = ABCMeta
    @abstractmethod
    def show(self, showable): raise NotImplementedError
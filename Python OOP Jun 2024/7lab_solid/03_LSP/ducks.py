from abc import ABC, abstractmethod


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class WalkingDuck(Duck, ABC):
    @staticmethod
    @abstractmethod
    def walk():
        pass


class FlyingDuck(Duck, ABC):
    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeak"


class RobotDuck(FlyingDuck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """Can only fly to a specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0

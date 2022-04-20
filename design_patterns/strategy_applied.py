from abc import ABC, abstractmethod


class TransporterInterface(ABC):

    @abstractmethod
    def get_duration(self):
        pass


class BikeStrategy(TransporterInterface):
    SPEED = 10
    BREAK_POINT = 4

    def get_duration(self, distance):
        return (distance / self.SPEED) + (self.BREAK_POINT * 0.25)

    def __str__(self) -> str:
        return 'bike'


class CarStrategy(TransporterInterface):
    SPEED = 100

    def get_duration(self, distance):
        return (distance / self.SPEED)

    def __str__(self) -> str:
        return 'car'


class BusStrategy(TransporterInterface):
    SPEED = 70
    BREAK_POINT = 2

    def get_duration(self, distance):
        return (distance / self.SPEED) + (self.BREAK_POINT * 0.25)

    def __str__(self) -> str:
        return 'bus'


class Navigator(object):

    def __init__(self, loc, dest, transportation) -> None:
        if dest < loc:
            raise ValueError(
                f"destination: {dest} must be greater than location: {loc}")
        self.loc = loc
        self.dest = dest
        self._transportation = transportation

    @property
    def transportation(self):
        return self._transportation

    @transportation.setter
    def transportation(self, transportation):
        self._transportation = transportation

    def print_duration(self):
        duration = self.transportation.get_duration(self.dest - self.loc)
        print(f'By {self.transportation} {duration:.2f} hour(s)')

    def run(self, is_paid_road=False):
        if is_paid_road:
            self.transportation.SPEED *= 2

        self.print_duration()


if __name__ == '__main__':
    while True:
        loc = int(input('Enter location: '))
        dest = int(input('Enter destination: '))
        is_paid_road = bool(
            int(input('Want to use paid road?: 1 for Yes, 0 for No :    ')))
        try:
            clss = input('Strategy: CarStrategy, BusStrategy, BikeStrategy:  ')
            strategy = globals()[clss]
        except:
            print('Enter valid strategy')

        navigator = Navigator(loc, dest, strategy())
        navigator.run(is_paid_road)

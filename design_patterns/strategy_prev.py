

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

    def print_duration(self, speed, break_point=0, is_paid_road=False):
        speed = speed * 2 if is_paid_road else speed
        duration = ((self.dest - self.loc) / speed) + break_point*0.25
        print(f'By {self.transportation} {duration:.2f} hour(s)')

    def run(self):
        if self.transportation == 'bike':
            self.print_duration(10, 4, False)
        if self.transportation == 'car':
            self.print_duration(100, 0, True)
        if self.transportation == 'bus':
            self.print_duration(70, 2, True)


if __name__ == '__main__':
    navigator2 = Navigator(10, 250, 'bike')
    navigator2.run()
    navigator1 = Navigator(10, 250, 'bus')
    navigator1.run()
    navigator3 = Navigator(10, 250, 'car')
    navigator3.run()

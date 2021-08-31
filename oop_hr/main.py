from abc import ABCMeta, abstractmethod


class WorkerInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'work') and
            callable(subclass.work) and
            hasattr(subclass, 'calculate_salary') and
            callable(subclass.calculate_salary) or
            NotImplemented
        )

    @abstractmethod
    def work(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def calculate_salary(self) -> float:
        raise NotImplementedError


class Employee(WorkerInterface):
    BASE_SALARY = 1000

    def __init__(self, no, name, year) -> None:
        super().__init__()
        self.__no = no
        self.__name = name
        self.__year = year

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"Employee {self.name} is working.")

    def calculate_salary(self):
        return self.__year * self.BASE_SALARY


class Manager(Employee):
    MANAGEMENT_PAYMENT = 10_000

    def __init__(self, no, name, year, department) -> None:
        super().__init__(no, name, year)
        self.__department = department

    def work(self) -> None:
        print(f"Manager {self.name} is working.")
        self._manage()

    def _manage(self) -> None:
        print(f'Manager {self.name} is managing.')

    def calculate_salary(self) -> float:
        return self.MANAGEMENT_PAYMENT + super().calculate_salary()


class Director(Manager):
    def __init__(self, no, name, year, department, bonus) -> None:
        super().__init__(no, name, year, department)
        self.__bonus = bonus

    def work(self) -> None:
        print(f"Director {self.name} is working.")
        self._manage()
        self._make_a_strategic_plan()

    def _manage(self) -> None:
        print(f'Director {self.name} is managing.')

    def _make_a_strategic_plan(self):
        print(f'Director {self.name} is making a strategic plan.')

    def calculate_salary(self) -> float:
        return self.__bonus + super().calculate_salary()


class HumanResources:
    def pay_salary(self, worker: WorkerInterface) -> None:
        salary = worker.calculate_salary()
        print(f'Paying {worker.name}, salary: {salary}')


if __name__ == '__main__':
    try:
        e = Employee(1, 'Adnan', 10)
        m = Manager(2, 'Kaya', 5, 'R&D')
        d = Director(3, 'Ibrahim', 3, 'Company', 20_000)

        e.work()
        m.work()
        d.work()
        print('_________HR__________')
        hr = HumanResources()
        hr.pay_salary(e)
        hr.pay_salary(m)
        hr.pay_salary(d)
    except Exception as e:
        raise e

"""Output

Employee Adnan is working.
Manager Kaya is working.
Manager Kaya is managing.
Director Ibrahim is working.
Director Ibrahim is managing.
Director Ibrahim is making a strategic plan.
_________HR__________
Paying Adnan, salary: 10000
Paying Kaya, salary: 15000
Paying Ibrahim, salary: 33000

"""
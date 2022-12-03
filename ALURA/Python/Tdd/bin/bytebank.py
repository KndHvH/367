from datetime import date


class Employee:
    def __init__(self, name, birthday, salary) -> None:
        self.__name = name
        self.__birthday = birthday
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def birthday(self):
        return self.__birthday

    @property
    def salary(self):
        return self.__salary

    def getAge(self):

        birthday = (self.__birthday).split('/')

        currentYear = date.today().year
        return currentYear - int(birthday[-1])  

    def getBonus(self):
        value = self.salary * 0.1
        if value > 1000:
            value = 0
        return value

    def __str__(self) -> str:
        return f'Employee({self.name}, {self.birthday}, {self.salary})'

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

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def last_name(self):
        nospace = (self.name.strip()).split(' ')
        return nospace[-1] if len(nospace) > 1 else None

    def __can_reduce(self):
        names = ['Braganca', 'Windsor', 'Bourbon', 'Yamato',
                 'Al saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self.last_name() in names) and (self.salary >= 100000)

    def salary_reduce(self):
        if self.__can_reduce():
            self.salary = self.salary*0.9

    def get_age(self):

        birthday = (self.__birthday).split('/')

        currentYear = date.today().year
        return currentYear - int(birthday[-1])

    def increase_salary_by_value(self, value):
        self.salary = self.salary + value

    def get_bonus(self):
        value = self.salary * 0.1
    
        if value > 1000:
            raise Exception('Salary too big')
        return value



    def __str__(self) -> str:
        return f'Employee({self.name}, {self.birthday}, {self.salary})'

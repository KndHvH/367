
from bin.bytebank import *


class Test_Class:

    def test_when_age_recieve_13_03_2000_must_return_22(self):

        entry = '13/03/2000'
        expect = 22

        test = Employee('test', entry, expect)
        guess = test.get_age()

        assert guess == expect

    def test_when_name_recieve_pedro_almeida_carvalho_must_return_carvalho(self):

        entry = ' Pedro Almeida Carvalho '
        expect = 'Carvalho'

        test = Employee(entry, '00/00/0000', 0)

        assert expect == test.last_name()

    def test_when_name_recieve_pedro_must_return_None(self):

        entry = ' Pedro '
        expect = None

        test = Employee(entry, '00/00/0000', 0)

        assert expect == test.last_name()

    def test_when_salary_reduce_receive_100000_and_Carlos_Braganca_must_return_90000(self):

        entry_salary = 100000
        entry_name = 'Carlos Braganca'
        expect = 90000

        test = Employee(entry_name, '00/00/0000', entry_salary)

        test.salary_reduce()

        assert expect == test.salary

    def test_when_salary_reduce_receive_100000_and_Carlos_Alberto_must_return_100000(self):

        entry_salary = 100000
        entry_name = 'Carlos Alberto'
        expect = 100000

        test = Employee(entry_name, '00/00/0000', entry_salary)

        test.salary_reduce()

        assert expect == test.salary

    def test_when_salary_reduce_receive_90000_must_return_90000(self):

        entry_value = 90000
        expect = 90000
        entry_name = 'Carlos Braganca'

        test = Employee(entry_name, '00/00/0000', entry_value)

        test.salary_reduce()

        assert expect == test.salary

    def test_when_increase_salary_receive_3000_and_1000_must_return_4000(self):

        entry_salary = 3000
        entry_increase = 1000
        expect = 4000

        test = Employee('name', '00/00/0000', entry_salary)

        test.increase_salary_by_value(entry_increase)
        assert expect == test.salary

    def test_when_getbonus_receive_5000_must_return_500(self):

        entry = 5000
        expect = 500

        test = Employee('name', '00/00/0000', entry)

        assert expect == test.get_bonus()

    def test_when_getbonus_receive_5000_must_set_salary_5500(self):

        entry = 5000
        expect = 5500

        test = Employee('name', '00/00/0000', entry)

        test.increase_salary_by_value(test.get_bonus())

        assert expect == test.salary

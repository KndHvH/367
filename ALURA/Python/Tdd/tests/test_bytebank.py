
from bin.bytebank import *
import pytest


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


    def test_when_get_bonus_receive_1000_must_return_100(self):

        entry = 1000
        expect = 100

        test = Employee('name', '00/00/0000', entry)

        assert expect == test.get_bonus()


    def test_when_get_bonus_receive_11000_must_return_exception(self):

        with pytest.raises(Exception):

            entry = 11000

            test = Employee('name', '00/00/0000', entry)

            test.get_bonus()


    def test_when_increase_salary_receive_1000_and_500_must_return_1500(self):

        entry_salary = 1000
        entry_increase = 500
        expect = 1500

        test = Employee('name', '00/00/0000', entry_salary)
        test.increase_salary_by_value(entry_increase)

        assert expect == test.salary
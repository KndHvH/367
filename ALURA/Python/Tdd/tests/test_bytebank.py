
from bin.bytebank import *


class Test_Class:

    def test_when_age_recieve_13_03_2000_must_return_22(self):

        entry = '13/03/2000'
        expect = 22

        test = Employee('test', entry, expect)
        guess = test.getAge()

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

    def test_when_salary_reduce_receive_100000_must_return_90000(self):

        entry = 100000
        expect = 90000

        test = Employee('Carlos', '00/00/0000', entry)

        test.salary_reduce()

        assert expect == test.salary

    def test_when_salary_reduce_receive_90000_must_return_90000(self):

        entry = 90000
        expect = 90000

        test = Employee('Carlos', '00/00/0000', entry)

        test.salary_reduce()

        assert expect == test.salary

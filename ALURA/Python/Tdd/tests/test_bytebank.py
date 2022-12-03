
from bin.bytebank import *


class Test_Class:

    def test_when_age_recieve_13_03_2000_must_return_22(self):

        entry = '13/03/2000'
        expected = 22

        test = Employee('test', entry, expected)
        guess = test.getAge()

        assert guess == expected

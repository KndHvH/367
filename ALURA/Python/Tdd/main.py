
from bin.bytebank import *


ana = Employee('Ana','13/03/1800', 10001)

print(ana)

ana.increase_salary_by_value(ana.get_bonus())


print(ana)
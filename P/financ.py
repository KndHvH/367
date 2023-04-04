import datetime

today = datetime.date.today()

year = today.year
month = today.month
month -=1

inmonth = 500
taxm = 13.88/12
total = 7952.12
tax = 0


while total < 1000000:
    str_date = str(month)+'/'+str(year)

    space1 = (20 - len(str_date))*'-'
    space2 = (20 - len(f'{total:.2f}'))*'-'
    space3 = (20 - len(f'{tax:.2f}'))*'-'

    print(f'Date:{str_date}{space1}Money: R${total:.2f}{space2}Tax:{tax:.2f}{space3}AddPerMonth:{inmonth}')

    total += inmonth
    tax = total * (taxm/100)
    total += tax

    month += 1
    if month == 13:
        month = 1
        year += 1
        inmonth += 500

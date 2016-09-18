day = input('Enter a day')
day = int(day)
month = input('Enter a month')
month = int(month)
year = input('Enter a year; last two digits only')
year = int(year)
combo = day * month
if year == combo:
    print('This date is magic')
else:
    print('This date is not magic')
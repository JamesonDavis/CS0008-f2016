packages = int(input('Enter number of packages purchased:'))
cost = 99
total = packages * cost
if packages >= 10 and packages <= 19:
    print('Discount', cost * packages * .1)
    print('Total', total - (total *.1))
elif packages >= 20 and packages <= 49:
    print('Discount', cost * packages * .2)
    print('Total', total - (total * .2))
elif packages >= 50 and packages <= 99:
    print('Discount', cost * packages * .3)
    print('Total', total - (total * .3))
elif packages >= 100:
    print('Discount', cost * packages * .4)
    print('Total', total - (total * .4))
else:
    print('Error')
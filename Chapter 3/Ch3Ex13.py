weight = int(input('Enter weight of package in pounds:'))
if weight <= 2:
    print('Shipping costs $1.50')
elif weight > 2 and weight <= 6:
    print('Shipping cost $3.00')
elif weight > 6 and weight <= 10:
    print('Shipping costs $4.00')
elif weight > 10:
    print('Shipping costs $4.75')
else:
    print('Error')
penny = 1
nickel = 5
dime = 10
quarter = 25
pennyamount = int(input('Enter number of pennies:'))
nickelamount = int(input('Enter number of nickels:'))
dimeamount = int(input('Enter number of dimes:'))
quarteramount = int(input('Enter number of quarters:'))
if penny * pennyamount + nickel * nickelamount + dime * dimeamount + quarter * quarteramount == 100:
    print("You have exactly one dollar")
elif penny * pennyamount + nickel * nickelamount + dime * dimeamount + quarter * quarteramount > 100:
    print("You have more than one dollar")
else:
    print("You have less than one dollar")
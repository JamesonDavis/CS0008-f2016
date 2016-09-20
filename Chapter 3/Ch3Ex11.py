book = int(input('Enter number of books purchased:'))
print("You have purchased this many books:")
print(book)
if book == 0:
    print("You have zero points")
elif book == 2:
    print("You have 5 points")
elif book == 4:
    print("You have 15 points")
elif book == 6:
    print("You have 30 points")
elif book >= 8:
    print("You have 60 points")
else:
    print("Error")
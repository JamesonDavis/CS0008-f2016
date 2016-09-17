number = input('Input a number')
number = int(number)
if number<0 or number>36:
    print('input a number between 1 and 36')
if number == 0:
    color = "green"
elif number>=1 and number<=10:
    if number % 2 == 0:
        color = 'black'
    else:
        color = 'red'
elif number>=11 and number<=18:
    if number % 2 == 0:
        color = 'red'
    else:
        color = 'black'
print("Your color is", (color))
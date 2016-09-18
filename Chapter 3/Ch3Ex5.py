mass = input('Enter mass of object')
mass = int(mass)
weight = mass * 9.8
if weight > 500:
    print('Object weighs too much')
elif weight < 100:
    print('Object weighs too little')
else:
    print(weight)
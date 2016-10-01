#First ask user to input unit system preference
#Input 'USC' or 'metric'
unit = input('Choose either USC or metric:')
#Ask for distance driven and how much gas was used. Use if-elif statement to properly follow user's unit system choice
#Define variables based on unit system used
#else statement placed at the end in case user inputs something other than USC or metric
if unit == 'USC':
    USC_distance = int(input('Enter number of miles travelled:'))
    USC_gas = int(input('Enter number of gallons of gas used:'))
elif unit == 'metric':
    metric_distance = int(input('Enter number of km travelled:'))
    metric_gas = int(input('Enter number of liters of gas used:'))
else:
    print('Error')
#Next if-elif statments used to convert unit system based on initial unit system choice
if unit == 'USC':
    metric_distance = USC_distance * 0.621371
    metric_gas = USC_gas *  0.264172
elif unit == 'metric':
    USC_distance = metric_distance * 1.60934
    USC_gas = metric_gas * 3.78541
else:
    print('Error')
#Now that four variables are defined at this point, we can calculate the gas consumption
USC_consumption = USC_distance // USC_gas
metric_consumption = (100 * metric_gas) // metric_distance
#Gas consumption rating can now be defined by using if-elif statements
if metric_consumption > 20:
    Gas_rating = 'Extremely poor'
elif metric_consumption <= 20 and metric_consumption > 15:
    Gas_rating = 'Poor'
elif metric_consumption <= 15 and metric_consumption > 10:
    Gas_rating = 'Average'
elif metric_consumption <= 10 and metric_consumption > 8:
    Gas_rating = 'Good'
elif metric_consumption <= 8:
    Gas_rating = 'Excellent'
else:
    print('Error')
#With all variables defined, we can now print out a results table
#table is formatted to have each value be rounded to three digits
print('USC', 'metric',)
print('Distance_____:', format(USC_distance, '.3f'), 'miles', format(metric_distance, '.3f'), 'km')
print('Gas__________:', format(USC_gas, '.3f'), 'gallons', format(metric_gas, '.3f'), 'liters')
print('Consumption__:', format(USC_consumption, '.3f'), 'mpg', format(metric_consumption, '.3f'), '1/100 km')
print('Gas Consumption Rating:', Gas_rating)
Mix = input('Input a primary color:')
Mix2 = input('Input another primary color:')
if (Mix == 'yellow' and Mix2 == 'red') or (Mix == 'blue' and Mix2 == 'yellow'):
    print('The mixture is Green')
elif (Mix == 'blue' and Mix2 == 'red') or (Mix == 'red' and Mix2 == 'blue'):
    print('The mixture is Purple')
elif (Mix == 'red' and Mix2 == 'yellow') or (Mix == 'yellow' and Mix2 == 'red'):
    print('The mixture is Orange')
else:
    print('Not a primary color')
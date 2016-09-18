length1 = input('Input length of rectangle 1')
length1 = int(length1)
width1 = input('Input width of rectangle 1')
width1 = int(width1)
length2 = input('Input length of rectangle 2')
length2 = int(length2)
width2 = input('Input width of rectangle 2')
width2 = int(width2)
rectangle1 = length1 * width1
rectangle2 = length2 * width2
if rectangle1 == rectangle2:
    print ('Area of Rectangle 1 equals the area of Rectangle 2')
elif rectangle1 > rectangle2:
    print ('Rectangle 1 has a greater area')
else:
    print ('Rectangle 2 has a greater area')
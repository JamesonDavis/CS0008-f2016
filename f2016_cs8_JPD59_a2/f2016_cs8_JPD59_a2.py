#
# needs standard header as shown in class
# with name, username, class and instructor name and so forth
#

#Function processFile is defined
#Creates a loop to read the file line by line
#Converts the string into an array
#Adds one for each line and adds the data together
#Removes the last line
#Returns with the total number of lines and total amount of data
def processFile(fh):
    partial_distance = 0
    line_number = 0
    for line in fh:
        line_number += 1
        line = line.rstrip("\n")
        temp = line.split(",")
        dist = float(temp[1])
        partial_distance += dist
    return line_number,partial_distance

#Function printKV is defined
#Prints out the info that is returned from the function
#Formats the key at n-length characters
#Formats the string so that it is 20 spaces long
#Formats the integer so that it is 10 spaces long
#Formats the float so that it is 10 spaces and 3 decimal spaces long
def printKV(key, value, klen = 0):
    if isinstance(value, str):
        # MN:  if you want to format a string and right justfy it, 
        #      you need to apply the method rjust to the variable containing the string itself
        # MN: also in this statments, value should be a string so the format string should %s
        ##print (str.rjust(klen, 0) + " " + format(value, '30,.f'))
        print (key.rjust(klen, ' ') + " " + format(value, '20s'))
    elif isinstance(value, int):
        # MN: same as above about the method rjust
        # MN: in this statement, value is an integer, so format string should be 'd'
        ##print (str.rjust(klen, 10) + " " + format(value, '10,'))
        print (key.rjust(klen, ' ') + " " + format(value, '10,d'))
    elif isinstance(value, float):
        # MN: same as above about the method rjust
        ##print (str.rjust(klen, 10) + " " + format(value, '10,.3f'))
        print (key.rjust(klen, ' ') + " " + format(value, '10,.3f'))

#Asks user for a file to input
#Sets total distance and total number = to 0
#Creates a loop to open the function, return, and quit
#Initializes the printKV function
total_distance = 0
total_number = 0
name = input('File to be read: ')
while name and name != "quit" and name != "Q":
    fh = open(name, 'r')
    partial_total_number, partial_distance = processFile(fh)

    # MN: output is not aligned
    printKV('Partial Total # of Lines: ', partial_total_number)
    printKV('Partial distance run: ', partial_distance)
    fh.close
    total_distance += partial_distance
    total_number += partial_total_number
    name = input('File to be read: ')

#Outputs total results after loop finishes outputting partial results
# MN: output is not aligned
printKV('Total # of lines: ', total_number)
printKV('Total Distance: ', total_distance)

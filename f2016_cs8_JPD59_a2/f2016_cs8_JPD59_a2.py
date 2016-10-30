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
        print (str.rjust(klen, 0) + " " + format(value, '30,.f'))
    elif isinstance(value, int):
        print (str.rjust(klen, 10) + " " + format(value, '10,'))
    elif isinstance(value, float):
        print (str.rjust(klen, 10) + " " + format(value, '10,.3f'))

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

    printKV('Partial Total # of Lines: ', partial_total_number)
    printKV('Partial distance run: ', partial_distance)
    fh.close
    total_distance += partial_distance
    total_number += partial_total_number
    name = input('File to be read: ')

#Outputs total results after loop finishes outputting partial results
printKV('Total # of lines: ', total_number)
printKV('Total Distance: ', total_distance)
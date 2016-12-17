# Name: Jameson Davis
# Instructor: Massimiliano Novelli
# Course: CS 0008-f2016
# Note: any code reused from assignment 3 is labeled

class participant:
    #class properties
    #participant name
    name = "None"
    #total distance run by the participant
    distance = 0
    #total number of runs by the participant
    runs = 0

    #class methods
    #initializer methods
    #__init__ initializes an instance of the class
    #all three properties are accounted for: name, distance and runs
    def __init__(self, name, distance = 0):
        #set name
        self.name = name
        #set distance if less than zero
        if distance > 0:
            #set distance
            self.distance = distance
            #set number of runs
            self.runs = 1

    #define addDistances to add single distance to distance accumulator
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1

    #addDistances adds an array of distances to distance accumulator
    def addDistances(self, distances):
        # loops over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1

    # return the name of the participant
    def getName(self):
        return self.name

    # return the total distance run computed
    def getDistance(self):
        return self.distance

    # return the number of runs
    def getRuns(self):
        return self.runs

    #convert values in object to strings
    #format "name" = right align of 20 characters
    #format "distance run" = total distance run with 9 digits, a decimal point and 4 decimals
    #format "runs" = 4 digits without any decimals
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

    #convert to csv(excel)
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

    #end defining class participant

#Function getDataFromFile originally written by Massimiliano Novelli
#function reads all lines in the file and processes them to be added to an output list
def getDataFromFile(file):
    # initialize output list
    output = []
    # create loop to read file line by line
    for line in open(file,'r'):
        # exclude first line that is the header, which will be identified as the word 'distance'
        if "distance" in line:
            # skip over that line
            continue
        # remove \n from the line and split line at ","
        temp1 = line.rstrip('\n').split(',')
        # try/except is used to avoid errors
        try:
            # append record to output list in the form of a dictionary with 2 keys: name and distance
            # remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            # here we catch all the lines that are incorrectly formatted
            # and we skipp them too
            print('Invalid row : '+ line.rstrip('\n'))
        # end try/except
    # end for
    # return data records
    return output

#Ask user to open master input file. Then open files within master input file.
masterFile = input('Please enter master file: ')
dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]

#Line 192 originally written by Massimiliano Novelli with one modified varible (sourceFiles)
#rawData is a list of all the records from each data file
#allows one long list to be created from data within multiple files
rawData = sum([getDataFromFile(file) for file in dataFiles],[])

#number of files
numberFiles = len(dataFiles)

#total number of lines
total_lines = len(rawData)

#total number distance run by every participant
total_distance = sum([item['distance'] for item in rawData])

#Initialize data container using a dictionary
participants = {}

#loop created to account for runners with multiple distances
for item in rawData:
    # if person appears more than once, appends run time to the end of the name
    # if it is new, initialize elements in the accumulators
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    # insert distance in the list for this participant
    # MN: this indentation is incorrect.
    #     you are going to add the distance run only ones for each participant
    #    participants[item['name']].addDistance(item['distance'])
    participants[item['name']].addDistance(item['distance'])

# initialize accumulators for max and min distances
# min distance run and name
min = { 'name' : None, 'distance': None }
# max distance run and name
max = { 'name' : None, 'distance': None }

# create another dictionary to store the number of appearances each runner has
appearances = {}

# computes the total distance run for each participant looping on all the participants
for name, object in participants.items():
    # get the total distance run by this participant using object from class participants
    distance = object.getDistance()
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if min['name'] is None or min['distance'] > distance:
        min['name'] = name
        min['distance'] = distance
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if max['name'] is None or max['distance'] < distance:
        max['name'] = name
        max['distance'] = distance
    # get number of runs, aka apparences from participant object
    runner_appearances = object.getRuns()
    # check if we need to initialize this entry
    if not runner_appearances in appearances.keys():
        appearances[runner_appearances] = []
    appearances[runner_appearances].append(name)

#calculate number of runners
total_participants = len(participants)

#calculate total number of runners with multiple appearances
multi_record_count = len([1 for item in participants.values() if item.getRuns() > 1])

#open and write to output file
f = open('f2016_cs8_JPD59_fp.data.output.csv', 'w')
f.write('name,records,distance\n')
# loop through all the participants
for name, object in participants.items():
    # write line in file
    f.write(object.tocsv() + '\n')
#close files
f.close()

#print all calculated variables with correct formatting
#interger = 5d
#float = 12.5f
#string = 20s
print('Number of input files read: ' + format(numberFiles, '5d'))
print('Total number of lines read: ' + format(total_lines, '5d'))
print("")
print('Total distance run: ' + format(total_distance, '12.5f'))
print("")
print('Maximum distance run: ' + format(max['distance'], '12.5f'))
print('  By participant: ' + format(max['name'], '20s'))
print("")
print('Minimum distance run: ' + format(min['distance'], '12.5f'))
print('  By participant: ', format(min['name'], '20s'))
print("")
print('Total number of participants: ' + format(total_participants, '5d'))
print('Number of participants with multiple records: ' + format(multi_record_count, '12.5f'))

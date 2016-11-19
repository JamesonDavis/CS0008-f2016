#Open master input file. Then open files within master input file.
dataSources= "f2016_cs8_a3.data.txt"
with open(dataSources) as fh:
    for line in fh:
        fh = open(dataSources, 'r')
        sourceFiles = fh.readlines()

#strip end of line command from file names
sourceFiles = [item.strip('\n') for item in sourceFiles]

#Initialize data container using a dictionary (person_distances) and a list (data)
person_distances = {}
data = []
#set default values for max and min values
max = 0
maxkey = 0
min = -1
minkey = 0
#set counter for number of input files
input_files = 0
#loop on all the data files
for source in sourceFiles:
    #open current data file for reading
    fh = open(source, "r")
    #loop on all lines
    for line in fh:
        #check if it is a header
        if not 'distance' in line:
            #read the whole file in
            data.append(line.strip('\n'))
            lines = sum(1 for lines in data)
            line = line.strip('\n')
            (key, val) = line.split(',')
            #if person appears more than once, appends run time to the end of the name
            if(key in person_distances):
                person_distances[key].append(float(val))
            else:
                person_distances[key] = [float(val)]
            val = float(val)
            #calculate max and min for all runners
            if(val > max):
                max = val
                maxkey = key
            if(val < min or min == -1):
                min = val
                minkey = key
    input_files += 1
    #close file
    fh.close()

#strip end of line command from each distance value
distances = [item.strip('\n').split(',')[1] for item in data]

#calculate sum of total distance
total_distance = sum(\
                    [float(item.strip('\n').split(',')[1])\
                     for item in data])

#while running through the list of people, counter keeps track of duplicate runners
#also keep a counter for the number of participants
#print each runner and time to output file (output file must be opened first)
multi_record_count = 0
total_participants = 0
f = open('f2016_cs8_JPD59_a3.data.output.csv', 'w')
for key in person_distances:
    if(len(person_distances[key])>1):
        multi_record_count +=1
    f.write(key)
    f.write(',')
    f.write(str(len(person_distances[key])))
    f.write(',')
    f.write(str(sum(person_distances[key])))
    f.write('\n')
    total_participants += 1
f.close()

print('Number of input files read: ', input_files)
print('Total number of lines read: ', lines)
print('Total distance run: ', total_distance)
print('Maximum distance run: ', max)
print('  By participant: ', maxkey)
print('Minimum distance run: ', min)
print('  By participant: ', minkey)
print('Total number of participants: ', total_participants)
print('Number of participants with multiple records: ', multi_record_count)
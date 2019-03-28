import numpy
import sys
import csv

'''
#convert init file to numpy array
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        x = numpy.array([0.00, 0.00, 0.00])
        if line_count != 0:
            if row[3] == "asks":
                x[0] = 1
            x[1] = row[1]
            x[2] = row[0]
        if line_count == 1:
            init = [x]
        elif line_count > 1 :
            init = numpy.append(init, [x], axis=0)
        line_count += 1
numpy.save("out", init) #change name of file depending on pair
'''




#convert update file to numpy array
init = numpy.array([0])
update = numpy.array([0])
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    previnit = True
    for row in csv_reader:
        y = numpy.array([0.00, 0.00, 0.00])
        x = numpy.array([0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])
        if line_count !=0:
            if row[7] == "initial":
                if row[0] == "asks":
                    y[0] = 1
                y[1] = row[6] #price
                y[2] = row[8] #initial volume
                if line_count == 1:
                    init = [y]
                else:
                    init = numpy.append(init, [y], axis=0)
            else:
                if row[9] == "bids":
                    x[0] = 1
                else:
                    x[0] = 2
                print(row[6])
                x[1] = row[6]#price
                x[2] = row[8]#remaining volume
                x[3] = row[5]#delta volume
                x[4] = row[2]#timestamp in seconds
                x[5] = row[3]#timestamp in milliseconds
                if row[7] == "cancel":
                    x[6] = 1
                elif row[7] == "place":
                    x[6] = 2
                elif row[7] == "trade":
                    x[6] = 3
                x[7] = row[1]#eventID
                if previnit:
                    update = [x]
                    previnit = False
                else:
                    update = numpy.append(update, [x], axis=0)
        line_count += 1
numpy.save(sys.argv[3], update) #change the name of the output file depending on the pair
numpy.save(sys.argv[2], init)
print(init)
print(update)

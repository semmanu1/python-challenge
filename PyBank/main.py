import os
import csv

month = 0
net = 0
count = 0
number = 0
total = 0
output = 0
rounded_output = 0
inc_mon = 0
dec_mon = 0

column1 = []
column2 = []
changes = []
duplicate_col = []

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader: 
        column1.append(row[0])
        column2.append(int(row[1]))

    for i in range(0, len(column2)):
        net = net + column2[i]

    for i in range(1, (len(column2))):
        number = column2[i] - column2[i-1]
        changes.append(int(number))
    
    for i in range(0, len(changes)):
        total += changes[i]
        output = total/(len(changes))
        rounded_output = round(output,2)

    for i in column2:
        duplicate_col.append(column2)
    
    column2.sort()
    greatest = column2[-1]
    smallest = column2[0]    


print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(len(column1)))
print('Total: $' + str(net))
print('Average Change: $' + str(rounded_output))
print('Greatest Increase in Profits: Feb-2012 ' + str(greatest))
print('Greatest Decrease in Profits: Sep-2013 ' + str(smallest))
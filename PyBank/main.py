import os
import csv
from statistics import mean
filename = 'budget_data.csv'

date = []
totals = []
difference = []
Counter = 0
tempTotalRow = 0
currentTotalRow = 0
TotalProfits = 0

with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        currentTotalRow = row[1]
        if int(tempTotalRow) > 0:
            difference.append(int(currentTotalRow) - int(tempTotalRow))
        date.append(row[0])
        totals.append(row[1])
        tempTotalRow = currentTotalRow
        TotalProfits = TotalProfits + int(currentTotalRow)
        # for i in range(0, (len(totals))):
        #     totals[i] = int(totals[i]) 
    totalAvg = mean(difference)
print("Total Months: " + str(len(totals)))
print("Total Profits/Losses: " + str(TotalProfits))
print("Average Change: " + str(totalAvg))
import os
import csv
from statistics import mean
import math

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
        maxTotal = max(row[1])
        currentTotalRow = row[1]
        
        if int(tempTotalRow) > 0:
            difference.append(int(currentTotalRow) - int(tempTotalRow))

        date.append(row[0])
        totals.append(int(row[1]))
        tempTotalRow = currentTotalRow
        TotalProfits = TotalProfits + int(currentTotalRow)

    totalAvg = mean(difference)
    GreatestIncreaseMonthIndex = totals.index(max(totals))
    GreatestDecreaseMonthIndex = totals.index(min(totals))

print("Total Months: " + str(len(totals)))
print("Total Profits/Losses: " + str(TotalProfits))
print("Average Change: " + str(totalAvg))
print("Greatest Increase in Profits: " + date[GreatestIncreaseMonthIndex] + " (" + str(max(totals)) + ")")
print("Greatest Decrease in Profits: " + date[GreatestDecreaseMonthIndex] + " (" + str(min(totals)) + ")")
#need to convert average change to be currency

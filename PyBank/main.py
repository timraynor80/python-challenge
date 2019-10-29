import os
import csv
filename = 'budget_data.csv'

date = []
totals = []
change_list = []

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvfile:
        date.append(row.split(",")[0])
        totals.append(row.split(",")[1])
        for i in range(0, len(totals)):
            totals[i] = int(totals[i])
print(totals) 

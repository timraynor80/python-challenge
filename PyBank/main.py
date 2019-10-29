import os
import csv
filename = 'budget_data.csv'

date = []
totals = []

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvfile:
        date.append(row.split(",")[0])
        totals.append(row.split(",")[1])
    print(len(date))
    print(len(totals))
    print(totals)
    print(date)

import os
import csv

BudgetData = 'budget_data.csv'
Date = []
ProfLoss = []
MonthlyDifference = []
CurMoValue = 0
Difference = []

with open(BudgetData, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        Date.append(row[0])
        ProfLoss.append(int(row[1]))

        if CurMoValue == 0:
            CurMoValue = int(row[1])
            PrevMoValue = CurMoValue   
        CurMoValue = int(row[1])
        Difference.append(int(CurMoValue) - int(PrevMoValue))
        PrevMoValue = CurMoValue

    print("Total Months: " + str(len(Date)))

    TotalProfits = sum(ProfLoss)
    TotalProfits = '${:,.2f}'.format(TotalProfits)
    print("Total Profits/Losses: " + str(TotalProfits))

    AverageChange = int(sum(Difference)) / (int(len(Difference)) - 1)
    AverageChange = '${:,.2f}'.format(AverageChange)
    print("Average Change: " + str(AverageChange))

    GreatestMonthIncreaseIndex = Difference.index(max(Difference))
    GreatestIncrease = Difference[GreatestMonthIncreaseIndex]
    GreatestIncrease = '${:,.2f}'.format(GreatestIncrease)
    print("Greatest Increase in Profits: " + Date[GreatestMonthIncreaseIndex] + " (" + GreatestIncrease + ")")
  
    GreatestMonthDecreaseIndex = Difference.index(min(Difference))
    GreatestDecrease = Difference[GreatestMonthDecreaseIndex]
    GreatestDecrease = '${:,.2f}'.format(GreatestDecrease)
    print("Greatest Decrease in Profits: " + Date[GreatestMonthDecreaseIndex] + " (" + GreatestDecrease + ")")
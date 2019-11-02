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
        #update lists for Date and ProfLoss with each row value
        Date.append(row[0])
        ProfLoss.append(int(row[1]))

        #set values for Current Month Value and Previous Month Value for use in calculating Difference each month. CurMoValue initially set to 0 to run first iteration. 
        if CurMoValue == 0:
            #set CurMoValue and PrevMoValue the same, which will return a 0 for the first value in the Difference list.
            CurMoValue = int(row[1])
            PrevMoValue = CurMoValue   
        #update CurMoValue for next calculation  
        CurMoValue = int(row[1])
        Difference.append(int(CurMoValue) - int(PrevMoValue))
        #update PrevMoValue for next loop
        PrevMoValue = CurMoValue
    
    #create and open output.txt file
    output = open("output.txt", "w") 

    print("Financial Analysis", file=output)
    print("------------------------------", file=output)
    print("Financial Analysis")
    print("------------------------------")
    #calculate Total Months by taking a count of values in Date.
    print("Total Months: " + str(len(Date)), file=output)
    print("Total Months: " + str(len(Date)))

    #Calculate TotalProfits with a sum of the values in ProfLoss.
    TotalProfits = sum(ProfLoss)
    #format to proper decimal sturcture. 
    TotalProfits = '${:,.2f}'.format(TotalProfits)
    print("Total Profits/Losses: " + str(TotalProfits), file=output)
    print("Total Profits/Losses: " + str(TotalProfits))

    #Calculate the average of monthly changes with a sum of the values in Difference,
    #divided by a count of values in Difference, subtracted by one to account for our intial value of 0, on the first month, where we had no Previous Month Value. 
    AverageChange = int(sum(Difference)) / (int(len(Difference)) - 1)
    #format to proper decimal sturcture. 
    AverageChange = '${:,.2f}'.format(AverageChange)
    print("Average Change: " + str(AverageChange), file=output)
    print("Average Change: " + str(AverageChange))

    #Find which iteration # in Difference is the Greatest Increase by using list.index(max(list), use this later to call in this and other lists. 
    GreatestMonthIncreaseIndex = Difference.index(max(Difference))
    #Assign GreatestIncrease by using the GreatestMonthIncreaseIndex number found above with list(index)
    GreatestIncrease = Difference[GreatestMonthIncreaseIndex]
    #format to proper decimal structure.
    GreatestIncrease = '${:,.2f}'.format(GreatestIncrease)
    #print the Greatest Increase results using a list(index) for the Date and the GreatestIncrease found above for the highest value in Difference.
    print("Greatest Increase in Profits: " + Date[GreatestMonthIncreaseIndex] + " (" + GreatestIncrease + ")", file=output)
    print("Greatest Increase in Profits: " + Date[GreatestMonthIncreaseIndex] + " (" + GreatestIncrease + ")")
  
    #Find which iteration # in Difference is the Greatest Decrease by using list.index(max(list), use this later to call in this and other lists. 
    GreatestMonthDecreaseIndex = Difference.index(min(Difference))
    #Assign GreatestDecrease by using the GreatestMonthDecreaseIndex number found above with list(index)
    GreatestDecrease = Difference[GreatestMonthDecreaseIndex]
    #format to proper decimal structure.
    GreatestDecrease = '${:,.2f}'.format(GreatestDecrease)
    #print the Greatest Decrease results using a list(index) for the Date and the GreatestDecrease found above for the highest value in Difference.
    print("Greatest Decrease in Profits: " + Date[GreatestMonthDecreaseIndex] + " (" + GreatestDecrease + ")", file=output)
    print("Greatest Decrease in Profits: " + Date[GreatestMonthDecreaseIndex] + " (" + GreatestDecrease + ")")

    output.close()
# Pybank Challenge Module 2

import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Analyze each of the following Values:
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

# Total number of months included in the dataset
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        total_months += 1

# Net total amount of "Profit/Losses" over the entire period

        total_pl = total_pl + int(row[1])    

# Greatest increase in profits (date and amount) over the entire period

    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

# Greatest decrease in profits (date and amount) over the entire period

    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

# Changes in "Profit/Losses" over the entire period, and then the average of those changes

    avg_change = sum(profits)/len(profits)

#Displaying in terminal
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Exporting .txt
output = open(os.path.join('analysis', 'output.txt') , 'w')

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
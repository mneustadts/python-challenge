import os
import csv 

csvpath = os.path.join('..','Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    month = []
    pnl = []
    pnl_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}")               
       
    for row in csvreader:
        month.append(row[0])
        pnl.append(row[1])
 
    pnl_int = map(int,pnl)
    total_pnl = (sum(pnl_int))

    i = 0
    for i in range(len(pnl) - 1):
        profit_loss = int(pnl[i+1]) - int(pnl[i])
        pnl_change.append(profit_loss)
    Total = sum(pnl_change)
    monthly_change = Total / len(pnl_change)
    
# Months of greatest change
    greatest_increase = max(pnl_change)
    m = pnl_change.index(greatest_increase)
    month_increase = month[m+1]
    
    greatest_decrease = min(pnl_change)
    n = pnl_change.index(greatest_decrease)
    month_decrease = month[n+1]


print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')

print(f"Total number of months:  ${str(len(month))}")

print(f"Total: ${str(total_pnl)}")
      
print(f"Average monthly change in pnl_changes : ${str(round(monthly_change,2))}")

print(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")

bank_file = os.path.join("..","analysis", "bank_data.txt")
with open(bank_file, 'w') as out_file:
    out_file.write("Financial Analysis\n")
    out_file.write("----------------------------\n")
    out_file.write("Total number of months: {str(len(month)}\n")
    out_file.write(f"Total:  ${str(total_pnl)}\n")
    out_file.write(f"Average Change:  ${str(monthly_change)}\n")
    out_file.write(f"Greatest Increase in Profits:  {month_increase} (${greatest_increase})\n")
    out_file.write(f"Greatest Decrease in Losses:  {month_decrease} (${greatest_decrease})\n")
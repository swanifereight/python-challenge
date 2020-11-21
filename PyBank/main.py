import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')
pathout = os.path.join('Resources', "Budget Analysis")

#define    
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0
   
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next (csvreader)
    #print(f"Header: {csv_header}")
    
    for row in csvreader:

        count_months += 1

        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months ==1):
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            months.append(row[0])

            profit_loss_changes.append(profit_loss_change)
            previous_month_profit_loss = current_month_profit_loss
sum_profit_loss = sum(profit_loss_changes)
average_profit_loss = round(sum_profit_loss/(count_months -1),2)

highest_change = max(profit_loss_changes)
lowest_change = min(profit_loss_changes)

highest_month_index = profit_loss_changes.index(highest_change)
lowest_month_index = profit_loss_changes.index(lowest_change)
#print(highest_month_index)

best_month = months[highest_month_index]
worst_month = months[lowest_month_index]





    
    #print statements

print("Financial Analysis")
print("-----------------------------")    
print(f"Total Months: {(count_months)}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in Lossses: {worst_month} (${lowest_change})")



with open(pathout, "w") as txt_file:

    txt_file.write("Financial Analysis")
    txt_file.write("-----------------------------")
    txt_file.write(f"Total Months: {(count_months)}")
    txt_file.write(f"Total: ${net_profit_loss}")
    txt_file.write(f"Average Change: ${average_profit_loss}")
    txt_file.write(f"Greatest Increase in Profits: {best_month} (${highest_change})")
    txt_file.write(f"Greatest Decrease in Lossses: {worst_month} (${lowest_change})")





    
    
    






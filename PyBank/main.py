import os
import csv

csv_path = os.path.join('..','Resources', 'budget_data.csv')

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
    print(f"Header: {csv_header}")
    
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
print(highest_month_index)



        #total_months.append(row[0])
        #total_profit.append(int(row[1]))
       
        #print(len(months))
        #print(sum(total_profit))
        

   #for x in range(len(total_profit)+1):
       # monthly_profit_change.append(total_profit[x+1]-total_profit[x])

    #max_increase_value = max(monthly_profit_change)
    #max_decrease_value = min(monthly_profit_change)

    #max_increase_value = max(monthly_profit_change).index(max(monthly_profit_change)) + 1
    #max_decrease_value = min(monthly_profit_change).index(min(monthly_profit_change)) + 1

    
    #print statements

#print("Financial Analysis")
#print("-----------------------------")    
#print(f"Total Months: {len(total_months)}")


    
    
    






import os
import csv

csv_path = os.path.join('..','Resources', 'budget_data.csv')

#Empty lists    
total_months = []
total_profit = []
monthly_profit_change = []

   
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next (csvreader)
    print(f"Header: {csv_header}")
    
    for row in csvreader:
    
        total_months.append(str(row[0]))
        total_profit.append(int(row[1]))
        print(len(total_months))
        print(sum(total_profit))

    for x in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[x+1]-total_profit[x])

    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)

    max_increase_value = max(monthly_profit_change).index(max(monthly_profit_change)) + 1
    max_decrease_value = min(monthly_profit_change).index(min(monthly_profit_change)) + 1
    


    
    
    

#net total amount of Profit/Losses over the entire period




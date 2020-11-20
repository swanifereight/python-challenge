import os
import csv

    
    
total_months = []
total_profit = []
monthly_profit_change = []

csv_path = os.path.join('..','Resources', 'budget_data.csv')

  
#total months included in the dataset
#import the csv file   
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next (csvreader)
    print(f"Header: {csv_header}")
    
    for row in csvreader:
 #net amount of profit and loss     
 #  #print(row[0])
    
        total_months.append(str(row[0]))
        total_profit.append(int(row[1]))
    print(len(total_months))
    print(sum(total_profit))

    revenue_change = []

    
    
    

#net total amount of Profit/Losses over the entire period
total_months = len(total_months)
profit_loss = 0
#find revenue change
for x in range(1, len(total_profit)):
    revenue_change.append((int(total_profit[x]) - int(total_profit[x-1])))

 revenue_average = sum(revenue_change)/ len(revenue_change)   

#greatest_increase = ["",0]
greatest_increase = max(revenue_change)
#greatest_decrease = ['',0]
greatest_decrease = min(revenue_change)



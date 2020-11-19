import os
import csv

    
    
total_months = []
total_profit = []
monthly_profit_change = []

csv_path = os.path.join('..','Resources', 'budget_data.csv')

  
#total months included in the dataset
   
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next (csvreader)
    
    for row in csvreader:
       #print(row[0])
    
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    print(len(total_months))
    print(sum(total_profit))
    
    
    

#net total amount of Profit/Losses over the entire period
#greatest_increase = ["",0]
#greatest_decrease = ['',0]


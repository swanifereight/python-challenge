import os
import csv

csv_path = os.path.join( 'Resources', 'election_data.csv')

#define
months = []
candidates = []



count_votes = 0



with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next (csvreader)
    print(f"Header: {csv_header}")
    print(csvreader)

    #for row in csvreader:
    
    for row in csvreader:
        count_votes += 1

    #print(count_votes)
    
        candidates.append(row[2])
        
    
    
    
        

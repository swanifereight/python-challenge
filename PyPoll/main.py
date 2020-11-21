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

   
    
    for row in csvreader:
        count_votes += 1

    #print(count_votes)
    
        candidates.append(row[2])
 
    #print(candidates)
    
    
    
    candidates_count_Khan = candidates.count("Khan")
    #candidates.count("Khan")
    #print(candidates_count_Khan)
    
    candidates_count_Correy = candidates.count("Correy")
    #candidates.count("Correy")
    #print(candidates_count_Correy)
    
    candidates_count_Li = candidates.count("Li")
    #print(candidates_count_Li)
    
    candidates_count_O = candidates.count("O'Tooley")
    #print(candidates_count_O)
    
    for item in candidates:
            khan_percent = format(((candidates_count_Khan/count_votes) * 100), '.3f')
        #print(khan_percent)
            li_percent = format(((candidates_count_Li/count_votes) * 100), '.3f')
        #print(li_percent)
            correy_percent = format(((candidates_count_Correy/count_votes) * 100), '.3f')
        #print(correy_percent)
            o_percent = format(((candidates_count_O/count_votes) * 100), '.3f')
        
        #print(o_percent)
        
        if khan_percent > max(correy_percent, li_percent, o_percent):
            winner = "Khan"
        elif correy_percent > max(kahn_percent, li_percent, o_percent):
            winner = "Correy"
        elif li_percent > max(correy_percent, kahn_percent, o_percent):
            winner = "Li"
        else:
            winner = "O'Tooley"


print("Election Results")
print("--------------------")
print(f"Total Votes: {count_votes}")
print("--------------------")
print(f"Khan: {khan_percent}% ({candidates_count_Khan})")
print(f"Correy: {correy_percent}% ({candidates_count_Correy})")
print(f"Li: {li_percent}% ({candidates_count_Li})")
print(f"O'Tooley: {o_percent}% ({candidates_count_O})")
print("--------------------")


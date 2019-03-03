# Import Libraries
import os
import csv

# Set File Path 
csvpath = os.path.join('election_data.csv')


#  Variables 
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""

# Read the csv File
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        # Find the total vote count
        total_votes += 1
        #Find the list of candidates a well as the number of
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # percentages for each candidate by pulling info from items in the candidates dictionary
        # candidates dictionary: key= Name value= the number of votes
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

        # Finding the winner using the candidates dictionary. 
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]


#Print tests
print("Election Results")

print("Total Votes: " + str(total_votes))

for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")

print("Winner: " + winner)





output = os.path.join("poll_results.txt")

with open(output,'w') as file:
    file.write("Election Results")
    
    file.write("Total Votes: " + str(total_votes))
    
    for key, value in candidates.items():
        file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
    
    file.write("Winner: " + winner)
    

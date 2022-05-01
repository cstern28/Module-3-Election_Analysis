# The data we need to retrieve.
#Add our dependencies
import csv
import os
# 1. The total number of votes cast.
# 2. A complete list of candidates who recived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources/election_results.csv')

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize variable, total vote
total_votes = 0

#Declare a new list
candidate_options = []

#Declare empty dictionaryy
candidate_votes = {}

#Declare candidate dictionary
candidate_votes = {"Raymon Anthony Doane": candidate_votes, "Diana DeGette": candidate_votes, "Charles Casper Stockham": candidate_votes}

#Declare variable that holds an empty string value for the winning candidate
winning_candidate = ""

#Declare variable for "winning count" equal to zero
winning_count = 0

#Declare variable for "winning_percentage" equals 0
winning_percent = 0

#Declare vote percentage variable
#vote_percentage = (candidate_votes/total_votes)*100

#open election results and read the file
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)

#Print each row in the cvs file
    for row in file_reader:
        #print(row)
        #2. Add to the total vote count
        total_votes += 1
        
        #Print the candidate name from each row.
        candidate_name = row[2]
        
        #IF the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) 
        
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        #2 retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #3 Calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        #4 Print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

        if (votes > winning_count) and (vote_percentage > winning_percent):
            winning_count = votes
            winning_percent = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    for candidate in candidate_votes:    
        winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percent:.1f}%\n"
            f"---------------------------\n")
    print(winning_candidate_summary)         
        
        
        #Add candidate name to list
        #candidate_options.append(candidate_name)
        #Get only unique candidate names
        
#3. Print the total votes    
#print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)
    
    #print(winning_candidate)

#Use the with statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:

#Write some data to the file
    #txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

# Perform analysis
#To-do: Read and analyze data here.
#Read the file object with the reader function.
    



print(election_data)
#Close the file
election_data.close()


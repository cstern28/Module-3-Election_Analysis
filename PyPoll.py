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

#open election results and read the file
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)
    

#Use the with statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:

#Write some data to the file
    #txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

# Perform analysis
#To-do: Read and analyze data here.
#Read the file object with the reader function.
    

#Print each row in the cvs file
    #for row in file_reader:
        #print(row)

print(election_data)
#Close the file
election_data.close()


# Module-3-Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes case.
2. Get a complete list of canddates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate received.
5. Determine the winner of the election based on popular vote.

## Resources
- Date Source: election_results.csv
- Softwarre: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Raymon Anthony Doane
  - Diana DeGette
  - Charles Casper Stockham
- The candidate results were:
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes.
  - Diana DeGette received 73.8% of the votes and 272,892 votes.
  - Charles Casper Stockham received 23% of the votes and 85,213 votes.
- The winner of the election was:
  - Diane DeGette, who received 73.8% of the votes and 272,892 votes.
- There were 3 counties in the election
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson received 10.5% of the votes and 38,855 votes
  - Denver received 82.8% of the votes and 306,055 votes.
  - Arapahoe received 6.7% of the votes and 24,801 votes.
- The county with the largest turnout was Denver.

### Refer to Image below for the Results
![Image](https://github.com/cstern28/Module-3-Election_Analysis/blob/main/Resources/Election_Code_Results.png)

## Election Audit Summary
This script used to find the election candidate winner and largest county turnout can be revitalized and used for any election. The script can be modified for any counties and candidates because the script looks in every row on the data. One would have to ensure the same header organization is consistent. For example row[1] means that in the second column from the excel file being read, pull that information for the county name. Another column could be added in the excel file for city and state and referenced accordingly in the Python script for row[x]. In addition, a column could be added in the excel file to signfiy the candidate's party affiliation. Another statistic can be shown in the summary that determines the percentage of candidates for each party affiliation in the election. There could also be historical data file that shows the statistics for the current election party affiliation based on prior 3 elections.

### Refer to Image below for Row[] Example
![Image](https://github.com/cstern28/Module-3-Election_Analysis/blob/main/Resources/Row_Example.png)

## Challenge Overview
The election was not a close race and Diana exceeded her competitor votes by a large amount. Denver won for the largest county turnout.

## Challenge Summary
The election analysis helped me understand Python coding better. For example, I learned that in "if" statements, the i in if cannot be capitalized. The white space matters and if the indentation is not accurately formatted, then the code will not run. Also, it's important to remember whether in a for loop or not when you add an if statement and a print. Sometimes, it would make sense to put outside the for loop depending on the situation. 

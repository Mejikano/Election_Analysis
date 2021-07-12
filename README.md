# Election_Analysis

### Resources
- Data source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code, 1.57

## 1. Overview of the Election Audit
The purpose of this election audit is for supporting the Board of Elections, this project computes an algorithm able to identify wining candidates, provide counties turnout break down and record the results on an audit file without manual intervention based on an election file. 

The process script will dinamically identify all candidates and counties and summarize the results.


## 2. Election Audit Results
In this particular case for the Colorado elections, the analysis shows that:

-There were "369,711" votes cast in the election.

-The counties turnouts were:
  - **Jefferson** "10.5%" of the vote and "38,855" number of votes.
  - **Denver** "82.8%" of the vote and "306,055" number of votes.
  - **Arapahoe** "6.7%" of the vote and "24,801" number of votes.

-The largest County Turnout was: Denver
  
-The candidates were:
  - Charles Casper Stockham
  - Diana DeGette 
  - Raymon Anthony Doane

-The candidate results were:
  - **Charles Casper Stockham** received "23.0%" of the vote and "85,213" number of votes.
  - **Diana DeGette** received "73.8%" of the vote and "272,892" number of votes.
  - **Raymon Anthony** Doane received "3.1%" of the vote and "11,606" number of votes.

-The winner of the election was:
  - **Diana DeGette**, who received **"73.8%"** of the vote and **"272,892"** number of votes.

Below the results summary written on the Audit file and shown on the terminal screen:

![Colorado Election Results](https://github.com/Mejikano/Election_Analysis/blob/main/Resources/Election_Terminal_Output.png)

## 3. Election Audit Summary

This python script can be re-used for future elections as long the election_results file format does not change, having the same layout will ensure that the program dinamically identify the candidates,  counties and associate the number of votes, % vs total votes, the winner candidate and the county with the largest vote turnout. 

Following code, reads each row from a given elections and dinamically retreives the candidates and counties within the file to account for number of votes, votes percentage and winner candidate, generating a candidate (candidate_votes) and county (county_votes) dictionaries with their corresponding unique candedate and county values and number of votes.


```
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in counties:

           # 4b: Add the existing county to the list of counties.
            counties.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```

For future elections below variables have to be changed, to specify the input election file - variable: **file_to_load** and output files to store the election audit - variable:**file_to_save**

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```

i.e assuming that this script runs in a server, the file name can be entered rather than hardcoding the path

```
filename=input("Please provide the election file name for running the audit")
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", filename)
```
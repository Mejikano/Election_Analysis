#1.Open the data file.
#2.Write down the names of all the candidates.
#3.Add a vote count for each candidate.
#4.Get the total votes for each candidate.
#5.Get the total votes cast for the election.

#Importing dependencies
import csv
import os

# Assign a variable for the file to load and the path.
filetpath = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(filetpath) as file:

# Print the file object.
    print(file)

# Assign a variable for the file to be created/written.
filetosave = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(filetosave, "w") as fileout:

# Write into the file .
    fileout.write("Counties in the Election\n")
    fileout.write("----------------------------\n")
    fileout.write("Arapahoe\nDenver\nJefferson")
#1. retrieve the file
#2  Total number of votes cast
#3. A complete list of candidates who received votes
#4. Total number of votes each candidate received
#5. Percentage of votes each candidate won
#6. The winner of the election based on popular vote#

# Add our dependencies.
import os
import csv

# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save a file from a path.

file_to_save = os.path.join("analysis", "eletion_analysis.txt")

outfile = open(file_to_save, "w")

outfile.write("Hellow world!")

outfile.close()

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    hearders = next(file_reader)
    print(hearders)

    for row in file_reader:
       print(row)

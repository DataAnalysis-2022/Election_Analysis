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

# 1. Initialize a total vote number

total_votes = 0

# Candidate options

candidate_options = []

# Declare a empty dictionary

candidate_votes = {}

# initialize winning name, vote counts, and percentage

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    hearders = next(file_reader)

    for row in file_reader:

       # 2. Add to the total vote count
       total_votes += 1

       # print the candiate name from each row

       candidate_name = row[2]

       # if not in the candidate list, then Add candidate name to the candidate list
       if candidate_name not in candidate_options :

            candidate_options.append (candidate_name)

            # tracking candidate vote cound

            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count

       candidate_votes[candidate_name] += 1

# determine the percentage of votes for each candidate by looping through the counts

for candidate_name in candidate_options:

    votes = candidate_votes[candidate_name]

    votes_percentage = float(votes) / float(total_votes) *100

    print(f"{candidate_name:>25} :      {votes_percentage:.1f} % ({votes:,}) \n")

    # determing winning vote count and candidate

    if (votes > winning_count) and (votes_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = votes_percentage

            # set the winning canditate equal to the candidate name

            winning_candidate = candidate_name


winning_candidate_summary = (

    f"-----------------------------------------\n"

    f"Winner:                   {winning_candidate}\n"

    f"Winning Vote Count:       {winning_count: ,}\n"

    f"Winning Percentage:       {winning_percentage: .1f} % \n"

    f"-----------------------------------------\n"

)

print(winning_candidate_summary)

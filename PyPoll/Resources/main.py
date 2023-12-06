import csv
import os

# File paths
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidates = []

# Read the CSV file
with open(file_to_load, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1
        
        # Get the candidate name from the row
        candidate = row[2]
        
        # Add the candidate to the list if not already present
        if candidate not in candidates:
            candidates.append(candidate)

# Print the total number of votes cast
print(f"Total Votes: {total_votes}")

# Print the list of candidates who received votes
print("Candidates who received votes:")
for candidate in candidates:
    print(candidate)
import csv
import os

# File paths
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_to_load, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1
        
        # Get the candidate name from the row
        candidate = row[2]
        
        # Add the candidate to the dictionary if not already present
        if candidate not in candidates:
            candidates[candidate] = 0
        
        # Increment the vote count for the candidate
        candidates[candidate] += 1

# Print the total number of votes cast
print(f"Total Votes: {total_votes}")

# Print the results for each candidate
print("Candidates Results:")
for candidate, votes in candidates.items():
    # Calculate the percentage of votes
    percentage = (votes / total_votes) * 100
    
    # Print candidate name, percentage of votes, and total votes
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if the current candidate has more votes than the previous winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print the winner of the election
print(f"\nWinner: {winner}")



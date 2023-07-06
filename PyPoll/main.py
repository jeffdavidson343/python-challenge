# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote



import csv
import os

csv_path = os.path.join('Resources', 'election_data.csv')
txt_path = os.path.join("analysis", "election_analysis.txt")

# keep track
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_cnadidate = ""
winning_count = 0
winning_percentage = 0

# read file
with open(csv_path) as election_data:
    csv_reader = csv.reader(election_data)
    headers = next(csv_reader)

    for row in csv_reader:
        
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# save to txt file
with open(txt_path, "w") as txt_file:

    # print final vote count in terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save final vote count in txt file
    txt_file.write(election_results)

    # the percentage of votes each candidate won
    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        # print candidate results in terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #  print candidate results in txt file
        txt_file.write(candidate_results)

    
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)    

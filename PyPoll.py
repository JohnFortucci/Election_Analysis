# Import the functions we need to use
import csv
import os


# Assign a variable for the HOME directory. 
Home_directory = os.path.expanduser( '~' )

# Assign a variable for the file to read from.
file_to_load = os.path.join(Home_directory,"Documents","RICE Course","Election_Analysis","Resources","election_results.csv")

# Assign a variable for the file to write to.
file_to_save = os.path.join(Home_directory,"Documents","RICE Course","Election_Analysis","analysis","election_analysis.txt")

# Use the open statement to open the file as a text file
print("File to write to  " + file_to_save)
print("File to read from " + file_to_load)
# Declare a list to candidates name
candidate_options = []

# Declare and empty dictionary
candidate_votes = {}

# 1. Initialize a total vote counter.
total_votes = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with reader function.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    #Print each row in the CSV file.

    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        
        # Get the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list , if they do not already exist.
        # Check if candidate exists in the list
        if candidate_name not in candidate_options:
            # Add to the candidate list
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote for this candidates count
        candidate_votes[candidate_name] += 1
    # Close the file
    election_data.close()

    # Save the results to the output text file

    with open(file_to_save,"w") as txt_file:
        

    # Determine the percentage of votes for each candidate by loopint through the counts
    # 1. Iterate through the candidate list
        election_results = (
                            f"\nElection Results\n"
                            f"--------------------------------------------------------\n"        
                            f"Total Votes: {total_votes:,}\n"
                            f"--------------------------------------------------------\n"  
                    )
        print(election_results, end="")

    
            # Save the final vote count to the text file.
        txt_file.write(election_results)
        for candidate_name in candidate_votes:
            print(candidate_name)
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]

            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)


            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            # 4. Print the candidate name and percentage of votes

            txt_file.write(candidate_results)
            print(f"{candidate_name}: received {vote_percentage:.1f}% of vote.")
        winning_candidate_summary = (f"--------------------------------------------------------\n"
                                     f"Winner             : {winning_candidate}\n" 
                                     f"Winning vote count : {winning_count:,}\n"
                                     f"Winning Percentage : {winning_percentage:.1f}%\n"
                                     f"--------------------------------------------------------\n"
                                    )
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
        txt_file.close()
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)
# print(winning_candidate)

# winning_candidate_summary = (f"--------------------------------------------------------\n"
#                             f"Winner             : {winning_candidate}\n" 
#                            f"Winning vote count : {winning_count:,}\n"
#                            f"Winning Percentage : {winning_percentage:.1f}%\n"
#                             f"--------------------------------------------------------\n")
#


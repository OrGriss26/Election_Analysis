# -*- coding: UTF-8 -*-
#"""PyPoll Homework Challenge Solution."""


# Add our dependencies.

import csv

import os


# Add a variable to load a file from a path.

file_to_load = os.path.join("resources", "election_results.csv")


# Add a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_results.txt")


# Initialize a total vote counter.

total_votes = 0


# Candidate Options and candidate votes.

candidate_options = []

candidate_votes = {}



# 1: Create a county list and county votes dictionary.

counties_options = []

counties_votes = {}


# Track the winning candidate, vote count and percentage

winning_candidate = ""

winning_count_candidate = 0

winning_percentage_candidate = 0


# Winning county, vote, count and percentage

winning_county = ""

winning_count_county = 0

winning_percentage_county = 0



# 2: Track the largest county and county voter turnout.
    
largest_county_turnout = ""

largest_county_turnout_count = 0

largest_county_percentage = 0


# Read the csv and convert it into a list of dictionaries

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)


    # Read the header

    headers = next(file_reader)


    # For each row in the CSV file.

    for row in file_reader:


        # Add to the total vote count

        total_votes += 1


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

        if county_name not in counties_options:


           # 4b: Add the existing county to the list of counties.

            counties_options.append(county_name)


            # 4c: Begin tracking the county's vote count.

            counties_votes[county_name] = 0



    # 5: Add a vote to that county's vote count.

        counties_votes[county_name] += 1


# Save the results to our text file.

with open(file_to_save, "w") as txt_file:


    # Print the final vote count (to terminal)

    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n\n"
        f"County Votes:\n")

    print(election_results, end="")

    txt_file.write(election_results)



   # 6a: Write a for loop to get the county from the county dictionary.

    for county in counties_votes:


        # 6b: Retrieve the county vote count.

        votes_county  =  counties_votes[county]


        # 6c: Calculate the percentage of votes for the county.

        vote_percentage_county = int(votes_county) / int(total_votes) * 100  


         # 6d: Print the county results to the terminal.

        counties_results = (
            f"{county}: {vote_percentage_county:.1f}% ({votes_county:,})\n")

        print(counties_results)


         # 6e: Save the county votes to a text file.

        txt_file.write(counties_results)
        

        # 6f: Write an if statement to determine the winning county and get its vote count.

        if (votes_county > winning_count_county) and (vote_percentage_county > winning_percentage_county):


            # If true

            winning_count_county = votes_county

            winning_percentage_county = vote_percentage_county

            winning_county = county



    # 7: Print the county with the largest turnout to the terminal.

    winning_county_summary = (
        f"\n----------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"----------------------------\n")

    print(winning_county_summary)



     # 8: Save the county with the largest turnout to a text file.

    txt_file.write(winning_county_summary)


    # Save the final candidate vote count to the text file.

    for candidate in candidate_votes:


       # Retrieve vote count and percentage

        votes_candidate  =  candidate_votes[candidate]

        vote_percentage_candidate = int(votes_candidate) / int(total_votes) * 100  
        
        candidate_results = (f"{candidate}: {vote_percentage_candidate:.1f}% ({votes_candidate:,})\n")


    # Print each candidate's voter count and percentage to the
    # terminal.

        print(candidate_results)


        #  Save the candidate results to our text file.

        txt_file.write(candidate_results)
        

        # Determine winning vote count, winning percentage, and candidate.

        if (votes_candidate > winning_count_candidate) and (vote_percentage_candidate > winning_percentage_candidate):
           
            winning_count_candidate = votes_candidate

            winning_percentage_candidate = vote_percentage_candidate
            
            winning_candidate = candidate  


    # Print the winning candidate (to terminal)

    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count_candidate:,}\n"
        f"winning Percentage: {winning_percentage_candidate:.1f}%\n"
        f"----------------------------\n")

    print(winning_candidate_summary)


    # Save the winning candidate's name to the text file
    
    txt_file.write(winning_candidate_summary)
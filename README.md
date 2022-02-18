# Election Analysis

The action of every &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; agent <br />
  into the world <br />
starts <br />
  from their physical selves. <br />




## Overview

The purpose of this election audit analysis , was to develop a script that would tabulate the election results from and input CSV files (CSV - Comma Separated Values file) of a state wide election. 

The criteria for tabulating the results are :- 
- Single vote option (1 congressional seat)
- Multiple candidates
- Multiple counties

The output of the script will be to both :- 
- Terminal 
- Text file stored locally

As part of the analysis the following will be calculated and determined :
- List of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- Winner of the election based on popular vote
- Voter turnout for each county
- Percentage of votes from each county out of the total count
- The county with the highest turnout

## Election Audit Results

### Summary Results

Below is a summary of the requested data based of the processing script on the the election data file supplied.

#### OVERALL ELECTION RESULTS

  - TOTAL NUMBER OF VOTES (Calculation : for every record : __total_votes = total_votes + 1__)
    - Total number of votes cast : 369,711
  - BREAKDOWN BY COUNTY
    - Total number of votes (Calcuation : for every unique county : __number_of_votes = number_of_votes + 1__)
      - __Jefferson__ number of votes __38,885__
      - __Denver__ number of votes __306,055__
      - __Arapahoe__ number of votes __24,801__
    - Percentage of votes (Calcuation : for every unique county : __county_percentage = float(number_of_votes) / float(total_votes) * 100__)
      - __Jefferson__ percentage of votes __10.5%__
      - __Denver__ percentage of votes __82.8%__
      - __Arapahoe__ percentage of votes __6.7%__
    - __Denver__ was the county with the largest number of votes (This is determine by looping through the __number_of_votes__ for each county and finding the largest count)
  - BREAKDOWN BY CANDIDATE
    - Total number of votes (Calcuation : for every unique candidate : __number_of_votes = number_of_votes + 1__)
      - __Charles Casper Stockham__ number of votes __85,213__
      - __Diana DeGette__ number of votes __272,892__
      - __Raymon Anthony Doane__ number of votes __11,606__
    - Percentage of votes (Calcuation : for every unique candidate : __candidate_percentage = float(number_of_votes) / float(total_votes) * 100__)
      - __Charles Casper Stockham__ percentage of votes __23.0%__
      - __Diana DeGette__ percentage of votes __73.8%__
      - __Raymon Anthony Doane__ percentage of votes __3.1%__
- ELECTION WINNER (Winner is determine by looping through the __number_of_votes__ for each candidate and finding the largest count)
    - Winner : Diana DeGette
    - Winning vote count : 272,892 
    - Winning vote percentage : 73.8%

# Election Audit Summary

## Introduction

As we have demonstrated the advatages of have a computer solution to tabulate the results of election and producing anaysis of utimate winner , along withe voting total and percentages by counties. The solution that has been developed support the processing and analysis of a single item being voted on It is felt that we could develop this solution further to better enhance the voting processing and therefore reduce the amount of effort by the state election commission.

## Proposed enhancement

### Enchance the results processing to process more than one item being voted on.

Typically on election day there are multiple items being voted on examples of these can be , but not limited to below :- 
- Federal - Presidential.
- Federal - Senate and Congressional offices.
- State   - Election for state offices.
- State   - State resolutions.
- County  - Commisioner positions.

It is assumed that for the different categories of the type of vote (Federal , State , County) will have different requirements.

####Federal
- A seperate summary file would need to be generated for only the federal votes , allowing this file to be sent to a federal election committee with the election results. The actual format of the file will be defined if this proposal moves forward.

####State
- A sperate file would be generated for the state results. The actual format of the file will be defined if this proposal moves forward.

####County
- A seperate file would be generated for each county containing the results of their county election results. The actual format of the file will be defined if this proposal moves forward.

#####Vote counting
- Federal and State categories would be calculated by votes state wide for the specific resolution.
- State resolution may not be a candidate name , it may just be a yes know.
- County categories would only be counted in those particular counties for the specific resolution.

#####Changes to the input file
The current input file has three columns.
Ballot ID , County , Candidate

A new input file will need to be designed the actual format of the file will be defined if this proposal moves forward, but would be similar to the example below. 

Ballot ID , Category , Resolution , County , Voter selection

Below is a sample of the input file is below

Ballot ID | Category | Resolution | County | Voter selection|
------|--------|--------|--------|--------|
1234|Federal|President / Vice Precident|Jefferson|Candidate 1|
1234|State|State AG|Jefferson|Candidate 2|
1234|State|Implement a state tax|Jefferson|Yes|
1234|County|County commisioner|Jefferson|Candidate 3|

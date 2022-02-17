# Election Analysis

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

##### TOTAL NUMBER OF VOTES
- Total number of votes cast : 369,711

###### ELECTION WINNER

  WINNER | WINNING VOTE COUNT|WINNING PERCENTAGE|
  ------ | :---------:|:----------:|
  __Diana DeGette__   |272,892     |      73.8%  |


###### BY COUNTY

  COUNTY | NUMBER OF VOTES|PERCENTAGE OF VOTES|
  ------ | :---------:|:----------:|
  __Jefferson__   |38,885     |      10.5%   |
  __Denver__     |306,055     |      82.8%            |
  __Arapahoe__| 24,801 | 6.7% |
  
  - __Denver__ had the largest number of votes with 306,055 votes cast.
  
###### BY CANDIDATE

  CANDIDATE | NUMBER OF VOTES|PERCENTAGE OF VOTES|
  ------ | :---------:|:----------:|
  __Charles Casper Stockham__   |85,213    |      23.0% |
  __Diana DeGette__     |272,892    |      73.8%           |
  __Raymon Anthony Doane__| 11,606 | 3.1% |



# Election_Analysis
## Project Overview
Assist a Colorado Board of Elections employee in an election audit of tabluated results for a US Conggressional precinct in Colorado. The employee has asked for the following in order to complete the election audit.
1. Calculate the total number of votes cast
2. Calculate the total number and percentage of votes for each county in the precinct
3. Determine the county with the largest number of voters
4. Calculate the total number and percentage of votes each candidate received
6. Determine the winner of the election based on popular vote
## Resources
* Data Source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code, 1.65.2
## Election-Audit Results
The analysis of the election show that:

* There were 369,711 votes cast in the election
* The counties and voter breakdown in the precinct were:
  * Jefferson County - Voter turnout was 10.5% of the vote and 38,855 total votes
  * Denver County - Voter turnout was 82.8% of the vote and 306,055 total votes
  * Arapahoe County - Voter turnout was 6.7% of the vote and 24,801 total votes
* Denver had the largest number of votes.
* The candidate results were:
  * Charles Casper Stockham received 23.0% of the vote and 85,213 of votes
  * Diana DeGette received 73.8% of the vote and 272,892 votes
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
* The winner of the elction was:
  * Diana DeGette, who received 73.8% of the vote and 272,892 votes
 
 The script that was used to perform this analysis tracked both the votes and percentage of votes per candidate, in addition to determining the winner of the popular vote as shown below:
 ![Code snapshot 1](https://user-images.githubusercontent.com/99205688/157983712-d6b88ec8-1907-48c0-83ac-9c60373abc25.JPG)

When this script ran, the output was saved to an easy-to-read txt.file:
 
![results](https://user-images.githubusercontent.com/99205688/157984141-40b37878-0bc9-4ed1-85e1-7f02daeaa58d.JPG)
## Election-Audit Summary
In summary, the script used in this election audit can be used, with some modification, for any election. This code could be modified to calculate vote and percentage totals per candidate in a rank choice voting election. The code would need to calculate if a candidate received at least 50% of the total vote in round one to declare a winner, or it would need to continue to check votes in subsequent rounds until a candidate reached at least 50% of the vote. The code could also be modified to calculate which candidate won the highest percentage of each county, which could help future candidates understand the demographics of each area.


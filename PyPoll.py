#Open the data file
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Create a filename variable to a direct or indirect path file
file_to_save = os.path.join("analysis","election_analysis.txt")
#Open the election results and read the file
with open(file_to_load) as election_data:
    #To Do: read and analyze data here
    file_reader = csv.reader(election_data)
    #print(election_data)
    headers = next(file_reader)
    print(headers)
#Write down the names of all candidates
#Add a vote count for each candidate
#Get total votes for each candidate
#Get total votes case for the election
# Close the file
#Create a filename variable to a direct or indirect path file
#file_to_save = os.path.join("analysis","election_analysis.txt")
#Using the with statement open the file as a text file
#with open(file_to_save,"w") as txt_file:
#Write three counties to file
    #txt_file.write("Counties in the Election\n------\nArapahoe\nDenver\nJefferson")
#Close the file


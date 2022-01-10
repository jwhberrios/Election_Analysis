#Pseudocode:
#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5 The winner of the election based on popular vote


#Direct access to file
#1. Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: perform analysis
    print(election_data)

#Indirect path to access file
#1. Import csv & os
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
#Open the election results and read the file.
with open(file_to_load) as election_data:

        #Print the file object.
        print(election_data)

#Write to files
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open() function with the "w" mode we will write data to the file 
outfile = open(file_to_save, "w")

#Write some data to the file
outfile.write("Hello World")

#Close the file
outfile.close()


#Using With Statement
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open() function with the "w" mode we will write data to the file 
with open(file_to_save, "w") as txt_file:  

    #Write some data to the file
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")

    #or
    txt_file.write(" or Arapahoe, Denver, Jefferson")

    #Listing counties on its own line
    txt_file.write("\n\nArapahoe\nDenver\nJefferson")

    #Skill Drill
    txt_file.write("\n\n\nCounties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")




# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

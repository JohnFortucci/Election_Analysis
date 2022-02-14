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
with open(file_to_load) as election_data:

    # Read the file object with reader function.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    print(headers)
    #Print each row in the CSV file.

    # for row in file_reader:
    #    print(row)

    election_data.close()



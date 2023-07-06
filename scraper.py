import re
import glob

# Regular expression pattern to match the public addresses
pattern = r"PubAddress: ([13][a-km-zA-HJ-NP-Z1-9]{25,34})"

# List all the text files in the current directory
file_list = glob.glob("*.txt")

# Iterate over each file
for file_name in file_list:
    with open(file_name, 'r') as file:
        text = file.read()

    # Find all the matches for the pattern
    matches = re.findall(pattern, text)

    # Write the matches to the output file
    with open("addresses.txt", 'a') as output_file:
        for match in matches:
            output_file.write(match + '\n')

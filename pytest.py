# Question 4

# Your code here . . .

from os import path

# Create a Custom Exception Class
class FileHandlingError(Exception):
    pass

# Ask the user for user input
input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")

try:
    # Check if the input file exists or not (handles File Not Found Error)
    if not path.exists(input_file):
        # Raise an exception using custom exception class
        raise FileHandlingError("Input file not found.")

    try:
        # Open the input file and outpof the input file
        with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
            # Loop to reverse each line
            for line in infile:
                # reverse words of a line algorithm
                reversed_line = ' '.join(line.strip().split()[::-1])
                # write the reversed line to the output file
                outfile.write(reversed_line + '\n')

    # Catch other IO exceptions
    except (PermissionError, IsADirectoryError,
            NotADirectoryError, UnicodeDecodeError, UnicodeEncodeError, OSError) as io_err:
        # Raise an exception using custom exception class
        raise FileHandlingError(f"{io_err}")

# Handles File Not Found Error
except FileHandlingError as ex:
    print("Unexpected Error: " + ex.args[0])
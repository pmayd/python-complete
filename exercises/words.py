"""Documentation strings, or docstrings, are standard ways of documenting modules, functions, methods, and classes"""                  
from collections import Counter


def words_occur():
    """words_occur() - count the occurrences of words in a file."""
    # Prompt user for the name of the file to use.
    
    # Open the file, read it and store its words in a list.                     

    # Count the number of occurrences of each word in the file.
       
    # Print out the results.

    return None


# this is a very important part of a module that will only be executed
# if this file is calles via command line or the python interpreter. 
# This if statement allows the program to be run as a script by typing python words.py at a command line
if __name__ == '__main__':
    words_occur()
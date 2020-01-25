"""Documentation strings, or docstrings, are standard ways of documenting modules, functions, methods, and classes"""                  
from collections import Counter


def words_occur():
    """words_occur() - count the occurrences of words in a file."""
    # Prompt user for the name of the file to use.
    file_name = input("Enter the name of the file: ")

    # Open the file, read it and store its words in a list.
    # read() returns a string containing all the characters in a file
    # and split() returns a list of the words of a string “split out” based on whitespace
    with open(file_name, 'r') as f:
        word_list = f.read().split()                                  

    # Count the number of occurrences of each word in the file.
    word_counter = Counter(word_list)
   
    # Print out the results.
    print(
        f'File {file_name} has {len(word_list)} words ({len(word_counter)} are unique).\n' # f-strings dont need a \ character for multiline usage
        f'The 10 most common words are: {", ".join([w for w, _ in word_counter.most_common(10)])}.'
        
    )

    return word_counter


# this is a very important part of a module that will only be executed
# if this file is calles via command line or the python interpreter. 
# This if statement allows the program to be run as a script by typing python words.py at a command line
if __name__ == '__main__':
    words_occur()
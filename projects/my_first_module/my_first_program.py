import sys


def main():
    print("this is our second test script file")
    print(sys.argv)


main()

# call with python script2.py arg1 arg2 3
# this is our second test script file
# ['script2.py', 'arg1', 'arg2', '3']

# You can see that the command-line arguments have been stored in sys.argv as a list of strings. 

"""
import sys


def main():
   contents = sys.stdin.read()
   sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))


main()

# This script reads its standard input and writes to its standard output whatever it reads,
# with all occurrences of its first argument replaced with its second argument. 
# Called as follows, the script places in outfile a copy of infile with all occurrences of zero replaced by 0: 

# python replace.py zero 0 < infile > outfile


"""
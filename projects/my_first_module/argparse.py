"""You can configure a script to accept command-line options as well as
arguments. The argparse module provides support for parsing different types of
arguments and can even generate usage messages.

To use the argparse module, you create an instance of ArgumentParser,
populate it with arguments, and then read both the optional and
positional arguments. This listing illustrates the module's use.
"""
from argparse import ArgumentParser # guess why this does not work...


def main():
    parser = ArgumentParser()

    # Positional arguments
    # those without a prefix character (usually ("-") and are required

    parser.add_argument("indent", type=int, help="indent for report")
    parser.add_argument("input_file", help="read data from this file")

    # Optional arguments

    parser.add_argument(
        "-f", "--file", dest="filename", help="write report to FILE", metavar="FILE"
    )
    parser.add_argument("-x", "--xray", help="specify xray strength factor")
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_false",
        dest="verbose",
        default=True,
        help="don't print status messages to stdout",
    )

    args = parser.parse_args()

    # The argparse module returns a Namespace object containing the arguments as attributes.
    # You can get the values of the arguments by using dot notation. 

    print("arguments:", args)


main()

# python opts.py -x100 -q -f outfile 2 arg2
# arguments: Namespace(filename='outfile', indent=2, input_file='arg2', verbose=False, xray='100')

# python opts.py -h





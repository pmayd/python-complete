"""take a csv as input and replaces the delimiter
"""
import sys


def main():
   contents = sys.stdin.read()

   sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()

# python projects\my_first_module\csv_replacer.py , : < "data\GLB.Ts+dSST.csv" > text.csv
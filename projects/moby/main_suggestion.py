from pathlib import Path


if __name__ == "__main__":

    punct = str.maketrans("",  "", "!.,:;-?")
    text_file = Path(__file__).parent.parent.parent.joinpath("data", "moby_01.txt")
    output_file = Path(__file__).parent.joinpath('words.txt')

    with open(text_file, 'r') as infile, open(output_file, "w") as outfile:
        for line in infile:
            # make all one case
            cleaned_line = line.lower()
            
            # remove punctuation
            cleaned_line = cleaned_line.translate(punct)
            
            # split into words
            words = cleaned_line.split()
            cleaned_words = "\n".join(words) + "\n"
            # write all words for line
            outfile.write(cleaned_words)
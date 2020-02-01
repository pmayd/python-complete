from pathlib import Path


if __name__ == "__main__":

    text_file = Path(__file__).parent.parent.parent.joinpath("data", "moby_01.txt")
    output_file = Path(__file__).parent.joinpath('words.txt')

    with open(text_file, 'r') as infile, open(output_file, "w") as outfile:
        for line in infile:
            # make all one case
            
            
            # remove punctuation
            
            
            # split into words
            
            
            # write all words for line
            outfile.write(cleaned_words)
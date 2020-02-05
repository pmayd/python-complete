#!/usr/bin/env python3

""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""
from pathlib import Path


def word_count(file: str):
    with open(Path(__file__).parent.parent.parent.joinpath('data', file)) as file:
        line_count = 0
        word_count = 0
        char_count = 0
        
        for line in file:
            line_count += 1

            words = line.strip().split()

            word_count += len(words)
            char_count += len(line)

    print(f"File has {line_count} lines, { word_count} words, {char_count} characters")


if __name__ == "__main__":
    word_count('faust.txt')



import doctest
import operator
from collections import Counter


def most_repeating_word(words: list) -> str:
    """
    Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return the string that contains the greatest number of repeated letters. In other words:

    for each word, find the letter that appears the most times
    find the word whose most-repeated letter appears more than any other

    Bonus: 
    - make function robust (empty list, etc)
    - add parameter to count all leters, only vowels or only consonants

    Examples:
    >>> most_repeating_word(['aaa', 'abb', 'abc'])
    'aaa'
    >>> most_repeating_word(['hello', 'wonderful', 'world'])
    'hello'
    >>> words = ['this', 'is', 'an', 'elementary', 'test', 'example']
    >>> most_repeating_word(words)
    'elementary'
    """
    word_counts = {word: most_repeating_letter_count(word) for word in words}

    return max(word_counts.items(), key=operator.itemgetter(1))[0]


def most_repeating_letter_count(word: str) -> int:
    return Counter(word).most_common(1)[0][1]


if __name__ == "__main__":
    doctest.testmod()

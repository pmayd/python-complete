import doctest

def word_stats(words: list):
    """Write a function that takes a list of words (strings). It should return a tuple containing three integers, representing the length of the shortest word, the length of the longest word, and the average word length.

    Examples:
    >>> word_stats(['test'])
    (4, 4, 4.0)
    >>> word_stats(['a', 'b', 'c'])
    (1, 1, 1.0)
    >>> word_stats(['a', 'ab', 'abc'])
    (1, 3, 2.0)
    """
    return len(min(words)), len(max(words)), sum(len(w) for w in words) / len(words)


if __name__ == "__main__":
    doctest.testmod()
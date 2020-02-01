"""
Pig Latin (www.wikihow.com/Speak-Pig-Latin) is a common children’s "secret" language in English-speaking countries. （It’s normally secret among children who forget that their parents were once children themselves.) The rules for translating words from English into Pig Latin are quite simple:

    pIf the word begins with a vowel (a, e, i, o, or u), then add way to the end of the word. So air becomes airway and eat becomes eatway.
    If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add ay. Thus, python becomes ythonpay and computer becomes omputercay.
"""

def pig_latin():
    word = input("Enter a word: ")

    if word[0] in 'aeiou': # startswith is much more noisy
        print(f'{word}way')
    else:
        print(f'{word[1:]}{word[0]}ay')


if __name__ == "__main__":
    pig_latin()
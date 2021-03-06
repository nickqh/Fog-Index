import re
import sys
from SyllableCounter import syllables
from CompoundWord import split


try:
    FileObject = open("TestDocument.txt", "r")
except FileNotFoundError:
    with open("FileNotFound.txt", "w+") as new_file:
        new_file.write("File does not exist, please try again by placing a valid file named 'TestDocument.txt' in "
                       "current directory")
    sys.exit(0)

file_contents = FileObject.read()


def counting():

    syllablecount = 0
    beg_each_Sentence = re.findall(r"\.\s*(\w+)", file_contents)
    capital_words = re.findall(r"\b[A-Z][a-z]+\b", file_contents)
    words = file_contents.split()
    for word in words:
        if word not in capital_words and len(word) >= 3: #all lower case words

            if syllables(word) >= 3 and len(split(word)) == 1:
                syllablecount += 1

        if word in capital_words and word in beg_each_Sentence: #beginning of each sentence is uppercase

            if syllables(word) >= 3:
                syllablecount += 1
    return syllablecount


def wordcount():
    # Regex to match all words, hyphenated words count as a compound words
    return len(re.findall("[a-zA-Z-]+", file_contents))


def sentencecount():
    #regex to count sentences, can end with a period, "?" or "!"
    return (len(re.split("[.!?]+", file_contents))-1)


FileObject.close()


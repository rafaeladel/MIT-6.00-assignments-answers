# Problem Set 5: Ghost
# Name:
# Collaborators:
# Time:
#

import random
from itertools import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program.

def get_data(p, w):
    print p , "turn."
    print "Current fragement: ", w
    char = raw_input(p + " says: ").lower()
    print
    return char

def get_score(p):
    global players
    players[p] += 1
    print p, " wins this time!"
    for index in players:
        print index, " : ", players.get(index, 0)

def end_game(word):
    global wordlist
    for test_word in wordlist:
        if word in test_word:
            if word == test_word and len(word) > 3:
                return True
            else:
                return False
    return True

def play_ghost():
    global word
    current_p, next_p = "Player 1", "Player 2"
    while True:
        char = get_data(current_p, word)
        while (char in string.ascii_letters) != True:
            char = raw_input("Please enter an alphabetic only: ").lower()
        word += char
        if end_game(word) :
            print "Fragement: ", word
            get_score(next_p)
            break
        current_p, next_p = next_p, current_p


if __name__ == "__main__":
    wordlist = load_words()
    players = {"Player 1":0, "Player 2":0}
    word = ""
    print "Welcome to Ghost!"
    play_ghost()
    while True:
        play_again = raw_input("Do you want to play again ? (y/n): ").lower()
        if play_again == "y":
            word = ""
            play_ghost()
        elif play_again == "n":
            break
        else :
            pass
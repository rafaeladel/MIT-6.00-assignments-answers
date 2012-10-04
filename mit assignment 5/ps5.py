# Problem Set 5: 6.00 Word Game
# Name:
# Collaborators:
# Time:
#

import random
import string
import time
import operator

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
total_sum = 0

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, time, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    current_sum = 0
    global total_sum
    for letter in word:
        current_sum += SCRABBLE_LETTER_VALUES[letter]
    if len(word) >= n:
        current_sum += 50
    current_sum = current_sum / time
    total_sum += current_sum
    return current_sum


def get_words_to_points(word_list):
	points_dict = {}
	for word in word_list:
		word_sum = 0
		for char in word:
			word_sum += SCRABBLE_LETTER_VALUES[char]
		points_dict[word] = word_sum
	return points_dict


def pick_best_word(hand, points_dict):
	word_list = {}
	for word in points_dict:
		formed_word = ""
		for char in hand:
			if char in word:
				formed_word += char			
		if len(formed_word) == len(word) :
			word_list[word] = points_dict[word]
	return max(word_list.iteritems(), key = operator.itemgetter(1))[0]
		
		
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for c in hand:
        print c,            # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
	
    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ...
    for c in word:
        if hand[c] == 1:
            del hand[c]
        elif hand[c] > 1:
            hand[c] -= 1
        else:
            pass
    return hand
    
def check_hand(hand, points_dict):
	"""
	check whether if the current hand can form a word or not
	"""
	for word in points_dict:
		char_word = ""		
		for char in hand:
			if char in word:				
				char_word += char			
		if len(char_word) == len(word):   # if the test word is the word from dict
			return True					
	return False		

#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...

    d_word = {}
    for c in word:
        d_word[c] = d_word.get(c, 0) + 1

    #print hand   for debugging
    #print d_word  for debugging

    for c in d_word:
        if hand.get(c, 0) < d_word.get(c, 0):
            return False

    if word in points_dict:
        return True
    else:
        return False


def get_word(hand, time_limit, points_dict):    
    print "Current hand: ",
    display_hand(hand)
    old_time = time.time()
    ##word = raw_input("Enter word, or a . to indicate that you are finished: ")
    word = pick_best_word(hand, points_dict)
    print "Computer said:" , word
    new_time = time.time()
    time_taken = new_time - old_time
    time_limit = time_limit - time_taken if time_limit - time_taken > 0 else 0.0
    print "It took %0.2f to provide an answer" % time_taken
    if time_limit > 0.0:
        print "You have %0.8f seconds left!" % time_limit
        time_exceed = False
    else:
        time_exceed = True    
    return word.lower(), time_taken, time_exceed

#
# Problem #4: Playing a hand
#


def play_hand(hand, time_limit, points_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    word, time_taken, time_exceed = get_word(hand, time_limit, points_dict)
    while len(hand) > 0 and word != ".":
        if time_exceed is not True:
            print
            if is_valid_word(word, hand, points_dict) == False:
                print "---------------------"
                print "Invalid word!"
                print "---------------------"
                print
                time_limit -= time_taken
                word, time_taken, time_exceed = get_word(hand, time_limit, points_dict)
                continue
            else:
                print "*********************"
                print word, " earned ", get_word_score(word, time_taken, HAND_SIZE), " points. Total: ", total_sum, " points."
                print "*********************"
                print
                time_limit -= time_taken
                if check_hand(update_hand(hand, word), points_dict) == False:
					print "No words can be formed with the current hand"
					break
                word, time_taken, time_exceed = get_word(hand, time_limit, points_dict)
        else:
            print "You have exceeded the time limit, your score is: ", total_sum
            break
            
    print "Total score: " , total_sum
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#


def play_game(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...

    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE)  # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            time_limit = float(raw_input("Enter time limit, in seconds: "))
            play_hand(hand.copy(), time_limit, points_dict)
            print
        elif cmd == 'r':
            if 'time_limit' not in locals():
                time_limit = float(raw_input("Enter time limit, in seconds: "))
            play_hand(hand.copy(), time_limit, points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    play_game(points_dict)

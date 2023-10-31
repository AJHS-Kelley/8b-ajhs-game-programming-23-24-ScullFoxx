# Hangman Game by Alexandra Sculley, v0.4
import random

words = 'purple orange red yellow violet blue teal green banana seagreen beige lavender crimson maroon coral cyan lime turquoise fuchisa olive vermillion aquamarine apricot sienna feldgrau smaragdine xanadu amaranth glaucous skobeloff'.split()

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
        +---+
            |
            |
            |
         ======= ''', '''
        +---+
        O   |
            |
            |
         =======''',''' 
        +---+
        O   |
        |   |
            |
         =======''', '''
        +---+
        O   |
       /|   |
            |
         =======''', '''
        +---+
        O   |
       /|\  |
            |
         =======''', '''
        +---+
        O   |
       /|\  |
       /    |
         =======''', '''
        +---+
        O   |
       /|\  |
       / \  |
         =======''']

# Pick word from list
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    #len(listName) is 1 is EXTREMELY COMMON FOR WORKING WITH  LISTS.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()
    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    # FINISH THURSDAY







# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1
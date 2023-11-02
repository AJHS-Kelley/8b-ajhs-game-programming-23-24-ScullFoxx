# Hangman Game by Alexandra Sculley, v0.8
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
    
    blanks = '_' * len(secretWord)

    # Replace blanks with correct letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter from A-Z and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed this letter, pick another.')
        elif guess not in 'abcedfghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the ENGLISH ALPHABET.')
        else:
            return guess  

def playAgain():
    print('Do you want to play again? \n Yes or no?')
    return input().lower().startswith('y')

# Introduce the Game 
print('Welcome to Hangman by Alexandra S.')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess




# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1
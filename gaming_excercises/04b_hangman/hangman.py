# Hangman Game by Alexandra Sculley, v1.2
import random
#words = 'purple orange red yellow violet blue teal green cyan lime beige lavender crimson maroon coral banana seagreen turquoise fuchisa olive vermillion aquamarine apricot sienna feldgrau smaragdine xanadu amaranth glaucous skobeloff'.split( )
# DICTIONARY VERSION
# Stored in Key:Value Pairs.
# Actual Dictionary Word (Key): Value (Definition)
# Uses {} to specify a dictionary.
words = {'Colors': 'lavender crimson coral seagreen fuchisa feldgrau smaragdine xanadu maroon purple turquoise olvie vermillion apricot sienna'.split(),
         'Animals': 'cow cat bat dog lion tiger leopard tortise turtle seasponge seaurchin squid'.split(),
         'Shapes': 'square triangle trapezoid diamond oval circle rhombus elipse'.split(),
         'Foods': 'cake hotdog hamburger salmon shrimp rice pancake waffles omlete'.split()}


# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
        +---+
            |
            |
            |
            |
         ======= ''', '''
        +---+
        O   |
            |
            |
            |
         =======''',''' 
        +---+
        O   |
        |   |
            |
            |
         =======''', '''
        +---+
        O   |
       /|   |
            |
            |
         =======''', '''
        +---+
        O   |
       /|\  |
            |
            |
         =======''', '''
        +---+
        O   |
       /|\  |
       /    |
            |
         =======''', '''
        +---+
        O   |
       /|\  |
       / \  |
            |
         =======''', '''
        +---+
        O   |
      o-|-o |
       / \  |
            |
         =======''', '''
        +---+
        O   |
      o-|-o |
       / \  |
      o   o |
         =======''']

# Pick word from list
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    #len(listName) is 1 is EXTREMELY COMMON FOR WORKING WITH  LISTS.
    return wordList[wordIndex]

# Pick word from Dictionar
def getRandomWord(wordDict): # Return a random word from the list.
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    #len(listName) is 1 is EXTREMELY COMMON FOR WORKING WITH  LISTS.
    return [wordDict[wordKey][wordIndex], wordKey]


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

# CHOOSE DIFFICULTY
difficulty = 'X'
while difficulty not in 'EMH':
    print('Please choose a difficulty between Easy, Medium, or Hard. Type the first letter then press enter.\n')
    difficulty = input().upper()
if difficulty == 'M': # MEDIUM
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
elif difficulty == 'H': # HARD
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]

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

    # Check to See If Winner, Winner Chikcen Dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord [i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters: # if True:
            print('Congrats you win.')
            print('The secret word was ' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have lost the game, ran out of guesses.')
            print('Your number of correct letters ' + str(len(correctLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else: 
            break

# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1
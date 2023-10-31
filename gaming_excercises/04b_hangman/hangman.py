# Hangman Game by Alexandra Sculley, v0.2

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

i = 0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1
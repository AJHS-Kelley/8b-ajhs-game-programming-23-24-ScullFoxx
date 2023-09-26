# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# add gamemodes
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left
    # Tell them if it's too high or too low
# What happens if the guess is right?
    # Tell them the guess is right.
    # Give them a point.
# What happens if the player runs out of guesses?
    # Tell player they lost that round.
    # Award point to cpu.
# Check to see if cpu or player has >= 3 points, if so they win. 



import random # Import the random module to our code

# DECLARATIONS
secretNumber = -1
playerGuess = -1 
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
gameMode = ""

print("""
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    |                             |
    |      Guess The Number       |
    |     alexandra sculley       |
    |           2023              |
    |                             |
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
     """)


# CPU SECRET NUMBER GENERATION
# secretNumber = random.randint(0, 50)
# print(secretNumber)

# GAME LOOP
print("You need to guess a number between different ranges, you have different amount of guesses per gamemode.\n Get it right, you get a point.\n Get it wrong, the CPU is awarded a point.\n First to 3 points wins")
gameMode = input("Please select your gamemode by typing Easy, Medium, Hard, or Impossible.\n")
if gameMode != "":
    playerName = input("Please insert your name.\n")
# playerName = input("Please insert your name.\n")
while playerScore != 3 and cpuScore != 3:
    # pass -- Tells python to skip this line of code
    print(f"{playerName}: {playerScore}\nCPU Score: {cpuScore}.\n")
    numGuesses = 0
    secretNumber = random.randint(0, 1000)
    if gameMode == "Impossible" or gameMode == "impossible":
        secretNumber = random.randint(0, 1000)
        # print(secretNumber)
        for guesses in range(8):
            print(f"You have {8 - numGuesses} remaining.")
            playerGuess = int(input("Type a number from 0 to 1000 and press ENTER.\n"))
            print(f"You have chosen {playerGuess}. Let's see if it's right!\n")
            if playerGuess == secretNumber:
                print("You've guessed it right! Congrats, here's a point.\n")
                playerScore += 1
                break
            else:
                print("Not quite, go ahead and give it another shot.\n")
                if secretNumber % 2 == 0:
                    print("Hint: The secret number is even!\n")
                else:
                    print("Hint: The secret number is odd!\n")
            
            if playerGuess > secretNumber:
                print("Your guess is too high!\n")
            else:
                print("Your guess is too low.\n")

            numGuesses += 1
    elif gameMode == "Hard" or gameMode == "hard" or gameMode == "hd":
        secretNumber = random.randint(0, 200)
        #print(secretNumber)
        for guesses in range(6):
            print(f"You have {6 - numGuesses} remaining.")
            playerGuess = int(input("Type a number from 0 to 200 and press ENTER.\n"))
            print(f"You have chosen {playerGuess}. Let's see if it's right!\n")
            if playerGuess == secretNumber:
                print("You've guessed it right! Congrats, here's a point.\n")
                playerScore += 1
                break
            else:
                print("Not quite, go ahead and give it another shot.\n")
                if secretNumber % 2 == 0:
                    print("Hint: The secret number is even!\n")
                else:
                    print("Hint: The secret number is odd!\n")
            
            if playerGuess > secretNumber:
                print("Your guess is too high!\n")
            else:
                print("Your guess is too low.\n")
            numGuesses += 1

    elif gameMode == "Medium" or gameMode == "medium" or gameMode == "med":
        secretNumber = random.randint(0, 50)
        #print(secretNumber)
        for guesses in range(4):
            print(f"You have {4 - numGuesses} guesses remaining.")
            playerGuess = int(input("Type a number from 0 to 50 and press ENTER.\n"))
            # input() saves all data as a STRING by default.
             # int() will convert it to an INTEGER.
            # float() will convert it to a FLOAT.
            print(f"You have chosen {playerGuess}. Let's see if it's right!\n")
            if playerGuess == secretNumber:
                print("You've guessed it right! Congrats, here's a point.\n")
                playerScore += 1
                break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
            else:
                print("Not quite, go ahead and give it another shot.\n")
                if secretNumber % 2 == 0:
                    print("Hint: The secret number is even!\n")
                else:
                    print("Hint: The secret number is odd!\n")
            
            if playerGuess > secretNumber:
                print("Your guess is too high!\n")
            else:
                print("Your guess is too low.\n")
            numGuesses += 1

    elif gameMode == "Easy" or gameMode == "easy" or gameMode == "ez":
        secretNumber = random.randint(0, 10)
        #print(secretNumber)
        for guesses in range(2):
            print(f"You have {2 - numGuesses} remaining.")
            playerGuess = int(input("Type a number from 0 to 10 and press ENTER.\n"))
            print(f"You have chosen {playerGuess}. Let's see if it's right!\n")
            if playerGuess == secretNumber:
                print("You've guessed it right! Congrats, here's a point.\n")
                playerScore += 1
                break
            else:
                print("Not quite, go ahead and give it another shot.\n")
                if secretNumber % 2 == 0:
                    print("Hint: The secret number is even!\n")
                else:
                    print("Hint: The secret number is odd!\n")
            
            if playerGuess > secretNumber:
                print("Your guess is too high!\n")
            else:
                print("Your guess is too low.\n")
            numGuesses += 1

    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins since you're out of guesses.\n")
        print(f"The secret number was {secretNumber}.\n")
if playerScore >= 3:
    print("Great game, you win this match!\n")
else:
    print("That's too bad, try guessing better next time.\n")
if cpuScore == 3:
    cpuScore += 1
elif playerScore == 3:
    playerScore += 1

        
    


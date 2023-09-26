# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
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
numAttempt = -1
rangeMin = -1
rangeMax = -1
cpuWon = 0
playerWon = 0

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
print(f"You need to guess a number between different ranges varying in difficulty, you have set number of guesses.\n Get it right, you get a point.\n Get it wrong, the CPU is awarded a point.\n First to 3 points wins")

playerName = input("Please insert your name.\n")
while True:
    print("Games Won")
    print(f"{playerName}:{playerWon}\n CPU:{cpuWon}")
    playerScore = 0
    cpuScore = 0
    while playerScore != 3 and cpuScore != 3:
        # pass -- Tells python to skip this line of code
        numGuesses = 0
        gameMode = input("Please select a difficulty between Easy, Medium, Hard, or Impossible.\n")
        print(f"{playerName}: {playerScore}\nCPU Score: {cpuScore}.\n")
        if gameMode == "Impossible" or gameMode == "impossible":
            rangeMin = 0
            rangeMax = 1000
            numAttempt = 4
        elif gameMode == "Hard" or gameMode == "hard":
            rangeMin = 0
            rangeMax = 200
            numAttempt = 6
        elif gameMode == "Medium" or gameMode == "medium":
            rangeMin = 0
            raneMax = 50
            numAttempt = 4
        elif gameMode == "Easy" or gameMode == "easy":
            rangeMin = 0
            rangeMax = 10
            numAttempt = 2
        secretNumber = random.randint(rangeMin, rangeMax)
        #print(secretNumber)
        #print(f"{rangeMin, rangeMax}")
        for guesses in range(numAttempt):
            print(f"You have {numAttempt - numGuesses} guesses remaining.")
            playerGuess = int(input(f"Type a number from {rangeMin} to {rangeMax} and press ENTER.\n"))
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
        if playerGuess != secretNumber:
            cpuScore += 1
            print("The CPU wins since you're out of guesses.\n")
            print(f"The secret number was {secretNumber}.\n")
        
    if playerScore >= 3:
        print("Great game, you win this match!\n")
        playerWon += 1
    else:
        print("That's too bad, try guessing better next time.\n")
        cpuWon += 1
                    
            
        


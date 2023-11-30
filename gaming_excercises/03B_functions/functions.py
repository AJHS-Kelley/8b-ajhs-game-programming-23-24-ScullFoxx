#8B 03_functions Sculley Alexandra, 10/25/23 v0.3
import random
# Function -- A named piece of code that can be used easily.
# Function signature -- Syntax for creatomg a new function.

def exampleFunctionA(): # no parameters
    count = 0
    num = int(input("How many times do you want to be wished happy birthday?\n"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1

def exampleFunctionB(num, count):
    while count < num:
        print("Happy Birthday!\n")
        count += 1



# If a function requires parameters, your code will crash without them!
# Returning a Fucntion is known as calling a function
#exampleFunctionA()
#exampleFunctionB(5, 0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
    return sum # Return will IMMEDIATELY exit a loop, function, if/elif/else blocks.
#rollDice(3, 6)
#rollDice(1, 20)

#strengthPlayer = rollDice(3, 6)
#dexterityPlayer = rollDice(3, 6)
#wisdomPlayer = rollDice(3, 6)

#print(strengthPlayer)
#print(dexterityPlayer)
#print(wisdomPlayer)

def genStats():
    playerStats = [
        0, # STRENGTH
        0, # DEXTERITY
        0, # CONSTITUTION
        0, # INTELLIGENCE
        0, # WISDOM
        0 # CHARISMA
        ]
    i = 0
    while i < len(playerStats):
        playerStats[i] = rollDice(3, 6)
        i += 1
    
    print(playerStats)

genStats()
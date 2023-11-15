# Fight Game, Alexandra Sculley, v0.1
import random
# Make characters
    # Assign them different attack, health, and defense stats
    # Give them names and make the character choose from them
# Introduce the game
# Print out character HP, different attacks to choose from, and differentiate from CPU.
# Give CPU a random character
# Start off with CPU then implement a 2 PLAYER system.

# FUNCTIONS DEFINED

def getChar(charcter):
    pass

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
    return sum

def genStats():
    playerStats = [
        0, # STRENGTH
        0, # HEALTH
        0  # DEFENSE
        ]
    i = 0
    while i < len(playerStats):
        playerStats[i] = rollDice(3, 6)
        i += 1




# ~~~ BEGINNING OF THE GAME TEXT ~~~
print("""
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    |                             |
    |          Welcome to         |
    |          FIGHT GAME         |
    |                             |
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
     """)



characterList = ["KYERIA",
    "WYMSICAL",
    "JEORDAN",
    "JONETHANE",
    "SKILDER",
    "OSTAINE",]
print(characterList)
picked = False
while picked == False:
    playerCharacter = input("Please type in a characters name to select them.\n").upper()
    if playerCharacter not in characterList:
        print(characterList)
        print("Please select a character from the list.")
    else:
        picked = True
        print(playerCharacter)

cpuChar = getChar(character)
while True:
 pass
 # Fight Game, Alexandra Sculley, v0.3
import random
# Make characters
    # Assign them different attack, health, and defense stats
    # Give them names and make the character choose from them
# Introduce the game
# Print out character HP, different attacks to choose from, and differentiate from CPU.
# Give CPU a random character
# Start off with CPU then implement a 2 PLAYER system.

# FUNCTIONS DEFINED
strength = 0
health = 0
defense = 0
cpuAttack = False
playerAttack = False

def getChar():
    getNum = random.randint(0, len(characterList) - 1)
    char = characterList[getNum]
    return char

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        #print(f"Roll: {roll}\n")
        #print(f"Sum: {sum}\n")
        numRolled += 1
    return sum

def genStats():
    playerStats = [
        0, # HELATH
        0, # STRENGTH
        0  # DEFENSE
        ]
    i = 0
    while i < len(playerStats):
        playerStats[i] = rollDice(3, 6)
        i += 1
    if playerStats[0] >= 6:
        health = 150
    else:
        health = 90
    if playerStats[1] >= 6:
        strength = 20
    else:
        strength = 10
    if playerStats[2] >= 6:
        defense = 30
    else:
        defense = 10
    print(f"Your health is {health}")
    print(f"You do about {strength} damage per hit.")
    print(f"You have {defense} extra health.")

def attackTime():
    if playerAttack == True:
        pass
    elif cpuAttack == True:
        cpuChar = 1
        pass


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
        print(f"You have selected {playerCharacter}")

cpuChar = getChar()
playerStats = genStats()
cpuStats = genStats()
print(f"CPU is character {cpuChar}")


while True:
    playerAttack = True 
    
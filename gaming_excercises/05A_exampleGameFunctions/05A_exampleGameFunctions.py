 # Fight Game, Alexandra Sculley, v0.5
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
playerAttack = True
playerStrength = 0
playerHealth = 0
playerDefense = 0
cpuStats = [0, 0, 0]
cpuStrength = 0
cpuHealth = 0
cpuDefense = 0
dmg = 0

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
    global playerHealth, playerStrength, playerDefense
    playerStats = [
        0, # HEALTH
        0, # STRENGTH
        0  # DEFENSE
        ]
    i = 0
    while i < len(playerStats):
        playerStats[i] = rollDice(3, 6)
        i += 1
    if playerStats[0] >= 6:
        playerHealth = 150
    else:
        playerHealth = 90
    if playerStats[1] >= 6:
        playerStrength = 20
    else:
        playerStrength = 10
    if playerStats[2] >= 6:
        playerDefense = 30
    else:
        playerDefense = 10
    print(f"Your health is {playerHealth}")
    print(f"You do about {playerStrength} damage per hit.")
    print(f"You have {playerDefense} extra health.")
    return playerHealth, playerStrength, playerDefense 

def genCpuStats():
    global cpuHealth, cpuStrength, cpuDefense
    cpuStats = [
        0, # HEALTH
        0, # STRENGTH
        0  # DEFENSE
        ]
    i = 0
    while i < len(cpuStats):
        cpuStats[i] = rollDice(3, 6)
        i += 1
    if cpuStats[0] >= 6:
        cpuHealth = 150
    else:
        cpuHealth = 90
    if cpuStats[1] >= 6:
        cpuStrength = 20
    else:
        cpuStrength = 10
    if cpuStats[2] >= 6:
        cpuDefense = 30
    else:
        cpuDefense = 10
    print(f"CPU's health is {cpuHealth}")
    print(f"CPU's strength is about {cpuStrength} damage per hit.")
    print(f"CPU has {cpuDefense} extra health.")
    return cpuHealth, cpuStrength, cpuDefense


def attackTime():
    global playerCharacter, cpuChar, playerStrength, playerDefense, playerHealth, cpuStrength, cpuDefense, cpuHealth, playerAttack, cpuAttack
    cpuHealth = cpuHealth + cpuDefense
    playerHealth = playerHealth + playerDefense
    fightStart = input("Fight?\n")
    if fightStart == "y":
        if playerAttack == True:
            cpuHealth = cpuHealth - damageRoll(playerCharacter)
            print(f"You did {damageRoll(playerCharacter)} damage to {cpuChar}! Leaving them with {cpuHealth} health.\n")
            playerAttack = False
            cpuAttack = True
        elif cpuAttack == True:
            playerHealth = playerHealth - damageRoll(cpuChar)
            print(f"CPU did {damageRoll(cpuChar)} damage to {playerCharacter}! Leaving you with {playerHealth} health.\n")
            playerAttack = True
            cpuAttack = False   
    elif fightStart == "n":
        print("You have chosen not to fight. Game over pacifist.") 
    else:
        print("y")
    
def damageRoll(char):
    global playerStrength, cpuStrength
    if char == cpuChar:
        dmg = random.randint(cpuStrength - 5, cpuStrength + 5)
    elif char == playerCharacter:
        dmg = random.randint(playerStrength - 5, playerStrength + 5)
    
    return dmg
    

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

playerStats = genStats()
cpuChar = getChar()
cpuStats = genCpuStats()
print(cpuStats)
print(playerStats)
print(f"CPU is character {cpuChar}")

while cpuHealth > 0 or playerHealth > 0:
    attackTime()
    if cpuHealth <= 0:
        print("You win! Trash cpu.")
    elif playerHealth <= 0:
        print("CPU wins! Trash player.")
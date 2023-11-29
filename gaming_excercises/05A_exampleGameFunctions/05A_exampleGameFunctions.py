 # Fight Game, Alexandra Sculley, v1.1
import random
# Make characters - Done
    # Assign them different attack, health, and defense stats - Done
    # Give them names and make the character choose from them - Done
# Introduce the game - Done
# Print out character HP, different attacks to choose from, and differentiate from CPU. - Done
# Give CPU a random character - Done
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
    print(f"You have {playerDefense} extra health.\n")
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
    fightStart = input("Fight?\n")
    insultList = ["Nerd.", "What's on your nose? My dick!", "You're going on my poopyhead list", "You're going on my reyp list", "Ur mom", "Baldy", "One two buckle my shoe three four buckle some more five six nike kicks head ahh", "Darth vader lookin ahh", "Where's waldo- Where's your dad!?", "Hey look up. Why's this dumbass lookin up?", "First I gyatt your brother, now I rizz you! Skibidi my friend!", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Say what if you're gay.", "*a mirror* . This you lil bro?"]
    superInsult = "You are utter bullshit at this game, go back to the sperm cells that made you."
    if fightStart == "yes":
        if playerAttack == True:
            playerChoice = input("Would you like to fight, heal, check player stats, check CPU stats, or INSULT.\n").lower()
            if playerChoice == "heal":
                if playerHealth == 180 or playerHealth == 120:
                    print("You're already at full HP! You've wasted your turn.")
                    playerAttack = False
                    cpuAttack = True
                else:
                    addedHealth = random.randint(1, 20)
                    playerHealth = playerHealth + addedHealth
                    print(f"You have healed for {addedHealth}. Your HP is now {playerHealth}.\n")
                    playerAttack = False
                    cpuAttack = True
            elif playerChoice == "fight":
                cpuHealth = cpuHealth - damageRoll(playerCharacter)
                print(f"You did {damageRoll(playerCharacter)} damage to {cpuChar}! Leaving them with {cpuHealth} health.\n")
                playerAttack = False
                cpuAttack = True
            elif playerChoice == "stats":
                print(f"PLAYER HEALTH: {playerHealth}\n PLAYER STRENGTH: {playerStrength} dph\n PLAYER DEFENSE: {playerDefense}\n")
            elif playerChoice == "cpu stats":
                print(f"CPU HEALTH: {cpuHealth}\n CPU STRENGTH: {cpuStrength} dph\n CPU DEFENSE: {cpuDefense}\n")
            elif playerChoice == "insult":
                rareInsult = random.randint(1, 100)
                if rareInsult < 100:
                    ranInsult = random.randint(0, len(insultList)-1)
                    #print(ranInsult)
                    insult = insultList[ranInsult]
                    print(insult)
                    additiveDamage = random.randint(10,30)
                    cpuHealth = cpuHealth - additiveDamage
                    print(f"The insult has hurt CPU's ego! CPU takes {additiveDamage} damage leaving it with {cpuHealth} HP!\n")
                    playerAttack = False
                    cpuAttack = True
                if rareInsult == 100:
                    print(superInsult)
                    additiveDamage = random.randint(75, 100)
                    cpuHealth = cpuHealth - additiveDamage
                    print(f"You've said the super insult, hurting CPU's ego MASSIVELY! CPU takes {additiveDamage} damage leaving it with {cpuHealth} HP!")
                    playerAttack = False
                    cpuAttack = True
        elif cpuAttack == True:
            cpuChoice = 2
            if cpuHealth < 180 or cpuHealth < 120:
                cpuChoice = random.randint(1,5)
            if cpuChoice == 1:
                addedHealth = random.randint(1, 20)
                cpuHealth = cpuHealth + addedHealth
                print(f"CPU has healed for {addedHealth}! CPU is now at {cpuHealth} HP.\n")
                cpuAttack = False
                playerAttack = True
            elif cpuChoice == 2:
                playerHealth = playerHealth - damageRoll(cpuChar)
                print(f"CPU did {damageRoll(cpuChar)} damage to {playerCharacter}! Leaving you with {playerHealth} health.\n")
                playerAttack = True
                cpuAttack = False
            elif cpuChoice == 3:
                print("CPU is checking your stats!")
                print(f"PLAYER HEALTH: {playerHealth}\n PLAYER STRENGTH: {playerStrength} dph\n PLAYER DEFENSE: {playerDefense}\n")
            elif cpuChoice == 4:
                print("CPU is checking its own stats!")
                print(f"CPU HEALTH: {cpuHealth}\n CPU STRENGTH: {cpuStrength} dph\n CPU DEFENSE: {cpuDefense}\n")
            elif cpuChoice == 5:
                rareInsult = random.randint(1, 100)
                if rareInsult < 100:
                    ranInsult = random.randint(0, len(insultList)-1)
                    insult = insultList[ranInsult]
                    print(insult)
                    additiveDamage = random.randint(10, 30)
                    playerHealth = playerHealth - additiveDamage
                    print(f"The insult has hurt your ego! {playerCharacter} takes {additiveDamage} damage leaving you with {cpuHealth} HP!\n")
                    playerAttack = True
                    cpuAttack = False
                elif rareInsult == 100:
                    print(superInsult)
                    additiveDamage = random.randint(75, 100)
                    playerHealth = playerHealth - additiveDamage
                    print(f"CPU has said the super insult, hurting your ego MASSIVELY! {playerCharacter} takes {additiveDamage} damage leaving you with {playerHealth} HP!")
                    playerAttack = True
                    cpuAttack = False
    elif fightStart == "no":
        print("You have chosen not to fight. Game over pacifist.") 
    else:
        print("y")
    
def damageRoll(char):
    global playerStrength, cpuStrength
    if char == cpuChar:
        dmg = random.randint(cpuStrength - 5, cpuStrength + 5)
        print(dmg)
    elif char == playerCharacter:
        dmg = random.randint(playerStrength - 5, playerStrength + 5)
        print(dmg)
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
print(f"CPU is character {cpuChar}")
cpuStats = genCpuStats()

cpuHealth = cpuHealth + cpuDefense
playerHealth = playerHealth + playerDefense

while cpuHealth > 0 or playerHealth > 0:
    attackTime()
    if cpuHealth <= 0:
        print("You win! Trash cpu.")
        break
    elif playerHealth <= 0:
        print("CPU wins! Trash player.")
        break
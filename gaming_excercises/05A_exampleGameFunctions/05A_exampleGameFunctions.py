 # Fight Game, Alexandra Sculley, v1.4
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
ply2Stren = 0
ply2Hp = 0
ply2Def = 0
ply2Char = ""
ply2Attack = False
gameMode = "cpu"
dmg = 0
bot = "on"
player2 = "off"

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

def gen2Stats():
    global ply2Hp, ply2Stren, ply2Def
    ply2Stats = [
        0, # HEALTH
        0, # STRENGTH
        0  # DEFENSE
        ]
    i = 0
    while i < len(ply2Stats):
        ply2Stats[i] = rollDice(3, 6)
        i += 1
    if ply2Stats[0] >= 6:
        ply2Hp = 150
    else:
        ply2Hp = 90
    if ply2Stats[1] >= 6:
        ply2Stren = 20
    else:
        ply2Stren = 10
    if ply2Stats[2] >= 6:
        ply2Def = 30
    else:
        ply2Def = 10
    print(f"{ply2Char}'s health is {ply2Hp}")
    print(f"{ply2Char}'s strength is about {ply2Stren} damage per hit.")
    print(f"{ply2Char} has {ply2Def} extra health.")
    return ply2Hp, ply2Stren, ply2Def


def attackTime():
    global playerCharacter, cpuChar, playerStrength, playerDefense, playerHealth, cpuStrength, cpuDefense, cpuHealth, playerAttack, cpuAttack, ply2Attack, ply2Char, ply2Attack, ply2Def, ply2Hp, ply2Stats, ply2Stren
    fightStart = input("Fight?\n")
    insultList = ["Nerd.", "What's on your nose? My dick!", "You're going on my poopyhead list", "You're going on my reyp list", "Ur mom", "Baldy", "One two buckle my shoe three four buckle some more five six nike kicks head ahh", "Darth vader lookin ahh", "Where's waldo- Where's your dad!?", "Hey look up. Why's this dumbass lookin up?", "First I gyatt your brother, now I rizz you! Skibidi my friend!", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Say what if you're gay.", "*a mirror* . This you lil bro?"]
    superInsult = "You are utter bullshit at this game, go back to the sperm cells that made you."
    if fightStart == "yes":
        if playerAttack == True:
            print("PLAYER TURN:")
            playerChoice = input("Would you like to fight, heal, check player stats, check other player stats, or INSULT.\n").lower()
            if playerChoice == "heal":
                if playerHealth == 180 or playerHealth == 120:
                    print("You're already at full HP! You've wasted your turn.")
                    if bot == "on":
                        playerAttack = False
                        cpuAttack = True
                    else:
                        playerAttack = False
                        ply2Attack = True
                else:
                    addedHealth = random.randint(1, 20)
                    playerHealth = playerHealth + addedHealth
                    print(f"You have healed for {addedHealth}. Your HP is now {playerHealth}.\n")
                    if bot == "on":
                        playerAttack = False
                        cpuAttack = True
                    else:
                        playerAttack = False
                        ply2Attack = True
            elif playerChoice == "fight":
                if bot == "on":
                    cpuHealth = cpuHealth - damageRoll(playerCharacter)
                    print(f"You did {damageRoll(playerCharacter)} damage to {cpuChar}! Leaving them with {cpuHealth} health.\n")
                    playerAttack = False
                    cpuAttack = True
                else:
                    ply2Hp = ply2Hp - damageRoll(playerCharacter)
                    print(f"You did {damageRoll(playerCharacter)} damage to {ply2Char}! Leaving them with {ply2Hp} health.\n")
                    playerAttack = False
                    ply2Attack = True
            elif playerChoice == "stats":
                print(f"PLAYER HEALTH: {playerHealth}\n PLAYER STRENGTH: {playerStrength} dph\n PLAYER DEFENSE: {playerDefense}\n")
            elif playerChoice == "other player stats":
                if bot == "on":
                    print(f"CPU HEALTH: {cpuHealth}\n CPU STRENGTH: {cpuStrength} dph\n CPU DEFENSE: {cpuDefense}\n")
                else:
                    print(f"PLAYER TWO HEALTH: {ply2Hp}\n PLAYER TWO STRENGTH: {ply2Stren}\n PLAYER TWO DEFENSE: {ply2Def}")
            elif playerChoice == "insult":
                rareInsult = random.randint(1, 100)
                if rareInsult < 100:
                    ranInsult = random.randint(0, len(insultList)-1)
                    #print(ranInsult)
                    insult = insultList[ranInsult]
                    print(insult)
                    additiveDamage = random.randint(10,30)
                    if bot == "on":
                        cpuHealth = cpuHealth - additiveDamage
                        print(f"The insult has hurt CPU's ego! CPU takes {additiveDamage} damage leaving it with {cpuHealth} HP!\n")
                        playerAttack = False
                        cpuAttack = True
                    else:
                        ply2Hp = ply2Hp - additiveDamage
                        print(f"The insult has hurt {ply2Char}'s ego! PLAYER 2 takes {additiveDamage} damage leaving it with {ply2Hp} HP!\n")
                        playerAttack = False
                        ply2Attack = True
                if rareInsult == 100:
                    print(superInsult)
                    additiveDamage = random.randint(75, 100)
                    if bot == "on":
                        cpuHealth = cpuHealth - additiveDamage
                        print(f"You've said the super insult, hurting CPU's ego MASSIVELY! CPU takes {additiveDamage} damage leaving it with {cpuHealth} HP!")
                        playerAttack = False
                        cpuAttack = True
                    else:
                        ply2Hp = ply2Hp - additiveDamage
                        print(f"You've said the super insult, hurting {ply2Char}'s ego MASSIVELY! PLAYER 2 takes {additiveDamage} damage leaving them with {ply2Hp}HP!")
                        playerAttack = False
                        ply2Attack = True
        elif cpuAttack == True and bot == "on":
            print("CPU TURN:")
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
        elif ply2Attack == True and player2 == "on":
            print("PLAYER TWO TURN:")
            player2Choice = input("Would you like to fight, heal, check player stats, check other player stats, or INSULT.\n").lower()
            if player2Choice == "heal":
                if ply2Hp == 180 or ply2Hp == 120:
                    print("You're already at full HP! You've wasted your turn.")
                    ply2Attack = False
                    playerAttack = True
                else:
                    addedHealth = random.randint(1, 20)
                    ply2Hp = ply2Hp + addedHealth
                    print(f"You have healed for {addedHealth}. Your HP is now {ply2Hp}.\n")
                    ply2Attack = False
                    playerAttack = True
            elif player2Choice == "fight":
                playerHealth = playerHealth - damageRoll(ply2Char)
                print(f"You did {damageRoll(ply2Char)} damage to {playerCharacter}! Leaving them with {cpuHealth} health.\n")
                ply2Attack = False
                playerAttack = True
            elif player2Choice == "stats":
                print(f"PLAYER TWO HEALTH: {ply2Hp}\n PLAYER TWO STRENGTH: {ply2Stren} dph\n PLAYER TWO DEFENSE: {ply2Def}\n")
            elif player2Choice == "other player stats":
                print(f"PLAYER 1 HEALTH: {playerHealth}\n PLAYER 1 STRENGTH: {playerStrength} dph\n PLAYER 1 DEFENSE: {playerDefense}\n")
            elif player2Choice == "insult":
                rareInsult = random.randint(1, 100)
                if rareInsult < 100:
                    ranInsult = random.randint(0, len(insultList)-1)
                    #print(ranInsult)
                    insult = insultList[ranInsult]
                    print(insult)
                    additiveDamage = random.randint(10,30)
                    playerHealth = playerHealth - additiveDamage
                    print(f"The insult has hurt {playerCharacter} ego! PLAYER 1 takes {additiveDamage} damage leaving them with {playerHealth} HP!\n")
                    ply2Attack = False
                    playerAttack = True
                if rareInsult == 100:
                    print(superInsult)
                    additiveDamage = random.randint(75, 100)
                    playerHealth = playerHealth - additiveDamage
                    print(f"You've said the super insult, hurting {playerCharacter} ego MASSIVELY! PLAYER 1 takes {additiveDamage} damage leaving it with {playerHealth} HP!")
                    ply2Attack = False
                    playerAttack = True

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
    elif char == ply2Char:
        dmg = random.randint(ply2Stren - 5, ply2Stren + 5)
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

gameMode = input("Would you like to PVP or play against CPU?").lower()
if gameMode == "cpu":
    bot = "on"
    player2 = "off"
    cpuChar = getChar()
    print(f"CPU is character {cpuChar}")
    cpuStats = genCpuStats()
elif gameMode == "pvp":
    bot = "off"
    player2 = "on"
    picked2 = False
    while picked2 == False:
        print(characterList)
        ply2Char = input("Please type in a characters name to select them.\n").upper()
        if ply2Char not in characterList:
            print(characterList)
            print("Please select a character from the list.\n")
        else:
            picked2 = True
            print(f"You have selected{ply2Char}")
ply2Stats = gen2Stats()
playerStats = genStats()
cpuChar = getChar()
print(f"CPU is character {cpuChar}")
cpuStats = genCpuStats()

cpuHealth = cpuHealth + cpuDefense
playerHealth = playerHealth + playerDefense
ply2Hp = ply2Hp + ply2Def
while cpuHealth > 0 or playerHealth > 0 or ply2Hp > 0:
    attackTime()
    if cpuHealth <= 0:
        print("You win! Trash cpu.")
        break
    elif playerHealth <= 0:
        print("CPU wins! Trash player.")
        break
    elif ply2Hp <= 0:
        print("Player 1 wins! Trash player 2.")
        break
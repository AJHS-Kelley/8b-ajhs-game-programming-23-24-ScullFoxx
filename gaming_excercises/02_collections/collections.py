# Collections Game, Alexandra Sculley, v0.2

# playerInventory = []

# while len(playerInventory) < 10:
#     item = input("What item would you like to add to the inventory?\n")
#     playerInvetory.append(item)

# playerInventory.sort()
# print(playerInventory)

# while len(playerInventory) > 5:
#     item = input("Which item would you like to remove from the inventory?\n")
#     playerInventory.remove(item)

# playerInventory.sort()
# print(playerInventory)

# doorKeys = [
#     "red",
#     "green",
#     "yellow",
#     "brown",
#     "purple"
# ]

# key = input("Which color key do you need to unlock the door?")

# if key in doorKeys:
#     print("You have the correct key! The door unlocks.\n")
# else:
#     print("You do not have that key. The door remains locked.\n")

weaponList = [
    True, # Battle axe
    False, # Ghost Sword
    False, # Flame Sword
    False, # Grenade Launcher
    True, # Suction Cups
    False, # Mucbane 
    True # God's Tears
]

weaponNum = 0
while weaponNum < len(weaponList):
    if weaponNum == 0 and weaponList[0] == True:
        print("You are wielding a Battle Axe.")
    if weaponNum == 1 and weaponList[1] == True:
        print("You are wiedling a Ghost Sword.")
    if weaponNum == 2 and weaponList[2] == True:
        print("You are wielding the Flame Sword.")
    if weaponNum == 3 and weaponList[3] == True:
        print("You are holding the Grenade Launcher.")
    if weaponNum == 4 and weaponList[4] == True:
        print("You are holding the Suction Cups.")
    if weaponNum == 5 and weaponList[5] == True:
        print("You are wielding the Muchbane.")
    if weaponNum == 6 and weaponList[6] == True:
        print("You are holding God's Tears.")
    weaponNum += 1
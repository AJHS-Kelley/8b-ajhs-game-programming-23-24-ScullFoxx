# Data Types and Operators, Alexandra Sculley, v0.5

# Variable Rules
# CANNOT START WITH A NUMBER!!!!!!!!!!!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED
# snake_case variables use _ to seperate words, all lower case
# camelCase variables do not use spaces, 1st word lower, rest upper.

# String Literal examples
playerName =  "Fooxly"
emptyString = ""
spaceString = " "
vegtableName = "toemawto"

# Integer Data Types
health = 100
extraLives = 5
temperature = -17
maidensAcquired = -2

# Floating Data Point Types
pi = 3.1415678
lapTime = 3.5
velocity = -2.0
damageTaken = 25.67

# Boolean Data Types
isFireType = False
weaponEquipped = True 
pvpEnabled = False 
isBurning = True

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS
print(3 + 3) # Addition
print(10 - 1) # Subraction
print(3 * -6) # Multiplication
print(10 / 5) # Division
print(6 ** 7) # Exponents
print(15 % 7) # MOD, will give you the remainder

# Comparison Operators 
print(5 > 3) # Greater than
print(7 >= 10) # Greater than OR Equal to
print(9 < 17) # Less than
print(7 <= 5) # Less than OR Equal to
print(8 == 6) # Is equal to
print(9 != 9) # Not equal to

# Assignment Operators
onePiece = "NOTHING" # Assign variable on the left to the value on the right, throw out any current value
ucp = (23 + 6)

# Addition Assignment
myWallet = 0
myWallet += 1
myWallet += 6
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print(3 > 5 and 4 < 3) # Requires both statements to be true
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
sunLight = "out"
rain = "no"
# print(sunLight = "out" and rain = "no") # Put variable most likely to be false first so it doesn't run through the whole thing

# Logical OR -- Requires ONE expression to be True.
print(3 > 6 or 5 < 8)
print(6 != 6 or 2 == 2)

# AND OR Combined
print("Line 80")
print(5 > 1 and 8 < 6 or 3 != 5)
# print(True and False or True)

# NOT Logical Operators
print(not (6 > 3))
print(not(not (not (3 != 6))))
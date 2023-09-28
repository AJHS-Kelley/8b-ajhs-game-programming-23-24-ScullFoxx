# Control Flow, Sculley Alexandra, v0.6
# Declarations

# favColor = "Purple"
# luckyNumber = 13
# myGPA = 3.1
# myAge = 16
# pineappleOnPizza = True
# favCharacter = "Chopper"

# If Statements - Check for a condition to be True/False, do something if true
# if favColor == "Purple":
#     print("Purple asf")

# if favCharacter == "Chopper":
#    print("W character fr")

# If-else statement -- Check for a condition, do something if false

# if myGPA >= 3.0:
#    print("smart ahh")
# else:
#    print("stupid ahh")

# if - eilf - else statements -- Checks for multiple conditions, if it something is True
# if myAge > 65:
#    print("dvmn u young")
# elif myAge > 50:
#    print("u still young")
# else:
#    print("we all get old someday")

# 1 if, 1 else, any number of elif allowed

# Nested if - elif - else statements
# if myGPA <= 1.5:
#    print("u finna fail lil bro")
# elif myGPA >= 2.0:
#  print(" ur on track for getting out of here")
# elif myGPA >= 3.0:
#    print("scholar ship money coming")
# elif myGPA >= 3.99:
#   print("def scholarship money")
# else:
#    print("no gpa")

# while loop -- think musical chairs -- used when you do not know how many iterations you need
# interation = one complete trip through a loop
x = 0
while x < 100:
    print(f"X is currently equal to {x}")
    x += 1


while x >= 0:
      print(f"X is currently equal to {x}")
      x -= 1

# For Loop -- Think 'Go Fish',  used when you know the number of iterations needed.
print("FOR LOOP STARTS HERE")

for i in range(10): # i = iterable variable
    print(i)

print("EVEN OR ODD LOOP HERE")

for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is Even!")
    else:
        print("That number is Odd!")




# (paranthesis)
# [brackets]
# {braces}
# <angle>
# Collections Examples, Alexandra Sculley, v0.2a

# LIST -- ORDERED, CHANGEABLE, ALLOWS DUPLICATE VALUES
breakfastFoods = ["Bacon", "waffles", "Panckes", "Cereal", "Milk"]
# Each item on the list is known as an ELEMENT.
# The position in the list for each item is the INDEX.
# The element "BACON" is at index 0.
# Python Only: index -1 is the last item on the list.  
testScores = [95, 100, 25, 15, 27, 35]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

# Printing Contents of an List
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

# Accessing Specific List Elements -- REMEMBER FIRST ELEMENT IS INDEX 0
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])

# Accessing Last Element in Lists
#print(breakfastFoods[-1])
#print(testScores[-1])
#print(classGPA[-1])

# Pause - WYOC -- Access the 3rd Element in Each List
elementTypes = ["Fire", "Light", "Sand", "Magma", "Ice"]
specialAngles = [45, 45, 90, 30, 60 ,90]
numberSeq = [1, 1, 2, 3, 5, 8, 13, 21, 34]

#print(elementTypes[2])
#print(specialAngles[2])
#print(numberSeq[2])

#print(breakfastFoods[2])
#print(testScores[2])
#print(classGPA[2])

# Change Items in a List
breakfastFoods[0] = "Sausage"
testScores[0] = 97
classGPA[0] = 3.57
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

# Pause -- WYOC -- Change 5th Element
elementTypes[4] = "Darkness"
specialAngles[4] = 45
numberSeq[4] = 6

breakfastFoods[4] = "Biscuits n Gravy"
testScores[4] = 35
classGPA[4] = 0.01
print(breakfastFoods)
print(testScores)
print(classGPA)
print(elementTypes)
print(specialAngles)
print(numberSeq)
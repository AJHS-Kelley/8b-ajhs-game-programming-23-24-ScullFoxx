# Collections Examples, Alexandra Sculley, v0.4c

# LIST -- ORDERED, CHANGEABLE, ALLOWS DUPLICATE VALUES
#breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk"]
# Each item on the list is known as an ELEMENT.
# The position in the list for each item is the INDEX.
# The element "BACON" is at index 0.
# Python Only: index -1 is the last item on the list.  
#testScores = [95, 100, 25, 15, 27, 35]
#classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

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

# Change Items in a List
#breakfastFoods[0] = "Sausage"
#testScores[0] = 97
#classGPA[0] = 3.57
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

# Pause -- WYOC -- Change 5th Element
#elementTypes[4] = "Darkness"
#specialAngles[4] = 45
#numberSeq[4] = 6
#print(elementTypes)
#print(specialAngles)
#print(numberSeq)

# Adding and Inserting Items of a List
# .append() adds an item to the END of a list.
#breakfastFoods.append("hash browns")
#print(breakfastFoods)
#testScores.append(99)
#print(testScores)
#classGPA.append(1.99)
#print(classGPA)

# .insert() allows you to place an item at a specific index in the list.
#breakfastFoods.insert(3, "Parfait")
#print(breakfastFoods)
#testScores.insert(3, 55)
#print(testScores)
#classGPA.insert(3, 0.0)
#print(classGPA)

#PAUSE -- WYOC -- .append() another item to each list. .insert() an item at index 5 to each list.
#elementTypes.append("Smoke")
#specialAngles.append(180)
#numberSeq.append(55)
#elementTypes.insert(5, "Water")
#specialAngles.insert(5, 360)
#numberSeq.insert(5, 13)
#print(elementTypes)
#print(specialAngles)
#print(numberSeq)

# Deleting Items from a List
# Use ,remove() to remove a specific item from the list.
#breakfastFoods.remove("Waffles")
#print(breakfastFoods)
#testScores.remove(100)
#print(testScores)
#classGPA.remove(2.25)
#print(classGPA) 

# To delete using the index value we use .pop()
#breakfastFoods.pop(4)
#print(breakfastFoods)
#testScores.pop(4)
#print(testScores)
#classGPA.pop(4)
#print(classGPA)

# PAUSE - WYOC -- .pop() the 2nd element from each list. .remove() any item from the list
#elementTypes.pop(1)
#specialAngles.pop(1)
#numberSeq.pop(1)
#elementTypes.remove("Magma")
#specialAngles.remove(90)
#numberSeq.remove(34)
#print(elementTypes)
#print(specialAngles)
#print(numberSeq)

# Determing List Length
#print(f"There are {len(breakfastFoods)} items in the breakfastFoods list.")
#print(f"There are {len(testScores)} scores in the testScores list.")
#print(f"There are {len(classGPA)} GPAs in the classGPA list.")

# List Methods -- Functions for working with lists.
# Sorting Lists -- Alphanumerical -- Ascending -- Capital Letters before Lower case letters.
#print(f"The original breakfastFoods list is {breakfastFoods}.")
#breakfastFoods.sort()
#print(f"The sorted breakfastFoods list is {breakfastFoods}.")
#print(f"The original testScores list is {testScores}.")
#testScores.sort()
#print(f"The sorted testScores list is {testScores}.")
#print(f"The original classGPA list is {classGPA}.")
#classGPA.sort()
#print(f"The sorted classGPA list is {classGPA}.")

breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk", "Pancakes"]
testScores = [95, 100, 25, 15, 27, 35, 100]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25, 2.25]

# .count() will return the number of times a value appears in a list.
#numWaffles = breakfastFoods.count("Waffles")
#print(f" There are {numWaffles} Waffles in the list.")
#numPancakes = breakfastFoods.count("Pancakes")
#print(f" There are {numPancakes} Pancakes in the list.")

# Pause -- WYOC -- Use .count() to count for a single item in the list and any multiple items. Use testScores and classGPA.

#num25s = testScores.count(25)
#print(f" There are {num25s} 25s in the list.")
#num100s = testScores.count(100)
#print(f" There are {num100s} 100s in the list.")
#num099s = classGPA.count(0.99)
#print(f" There are {num099s} 0.99s in the list.")
#num225s = classGPA.count(2.25)
#print(f" There are {num225s} 2.25s in the list.")

# Deleting All Contents of a List -- .clear()
#breakfastFoods.clear()
#print(f"The breakfast foods list is {breakfastFoods}.")
#testScores.clear()
#print(f"The testScores List is {testScores}.")
#classGPA.clear()
#print(f"The classGPA list is {classGPA}.")

# Common Bugs -- Index Out Of Range
print(f"The last item in the list is {breakfastFoods[4]}.")

print(f"The last item in the testScores list is {testScores[len(testScores) - 1]}.")
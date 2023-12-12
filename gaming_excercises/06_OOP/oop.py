# Object-Oriented Programming, Alexandra Sculley, v0.4

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight): 
        self.name = name
        self.age = age
        self.weight = weight

    # To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"
    
    def classFunction(self):
        print("This is an example class function.\n")
        print("It only works when called on an object of that class.\n")


person1 = Person("Lykia",25 ,135)
person2 = Person("Sylvia", 19, 122)
#print(person1)
#print(person2)

#if person1.weight > person2.weight:
#    print(f"{person1.name} weights more than {person2.name}.\n")
#elif person1.weight == person2.weight:
#    print("Each person weighs the same.\n")
#else:
#    print(f"{person2.name} weights more than {person1.name}.\n")

#if person1.age > person2.age:
#    print(f"{person1.name} is older than {person2.name}.\n")
#elif person1.age == person2.age:
#    print("Each person is the same age.\n")
#else:
#    print(f"{person2.name} is older than {person1.name}.\n")

#person1.classFunction()

#Changing Properties After Creation
#print(f"Person 1's original name is {person1.name}.\n")
#person1.name = "Christi"
#print(f"Person 1's new name is {person1.name}.\n")

#print(f"Person 2's original weight is {person2.weight}.\n")
#person2.weight = 100
#print(f"Person 2's new weight is {person2.weight}.\n")

# Deleting Properties -- DANGER WILL ROBINSON, DANGER!
# THIS DOES NO 'RESET' A PROPERTY, IT DELETES IT COMPLETELY.
#print(person1.name)
#del person1.name
#print(person1.name)

#print(person2.weight)
#del person2.weight
#print(person2.weight)

# Deleting Objects -- Delete them if you're finished with them.
#del person1

# Adding Properties to Objects -- USE CAREFULLY
person2.weakness = "Kryptonite"
print(person2)
print(person2.weakness)

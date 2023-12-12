# Object-Oriented Programming, Alexandra Sculley, v0.2

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight): 
        self.name = name
        self.age = age
        self.weight = weight

    # To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds. \n"


person1 = Person("Lykia",25 ,135)
person2 = Person("Sylvia", 19, 122)
print(person1)
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name} weights more than {person2.name}.\n")
elif person1.weight == person2.weight:
    print("Each person weighs the same.\n")
else:
    print(f"{person2.name} weights more than {person1.name}.\n")

if person1.age > person2.age:
    print(f"{person1.name} is older than {person2.name}.\n")
elif person1.age == person2.age:
    print("Each person is the same age.\n")
else:
    print(f"{person2.name} is older than {person1.name}.\n")
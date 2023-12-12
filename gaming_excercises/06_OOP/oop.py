# Object-Oriented Programming, Alexandra Sculley, v0.1

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight): 
        self.name = name
        self.age = age
        self.weight = weight

    # To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds. \n"


person1 = Person("Lykia",25 ,135)
print(person1)

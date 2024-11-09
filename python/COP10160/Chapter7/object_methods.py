class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old.")
    
    def greet(self, person):
        if person.name == "Rogers":
            print("Hey neighbour!")
        else:
            print(f"Hi {person.name}")

joe = Person("Josef", 31)
gabby = Person("Gabriela", 32)
john = Person("John", 5)
rogers = Person("Rogers", 46)

joe.greet(gabby)
john.greet(rogers)

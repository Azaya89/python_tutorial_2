# Object Oriented Programming aka OOP - A way to represent real life objects in python

# parent class
class Animal:
    def __init__(self, legs=4, tail=1, eyes=2, location='Bush'):
        self.legs = legs
        self.tail = tail
        self.eyes = eyes
        self.habitat = location

    def __repr__(self):
        return f"Animal(Legs: {self.legs}, Tail: {self.tail}, Eyes: {self.eyes})"

    def make_sound(self):
        return "Whooo!"

# child class
class Dog(Animal):
    def __init__(self, location='House'):
        super().__init__()
        self.habitat = location
    def make_sound(self):
        return "Woof! Woof!!"

bingo = Dog()
lion = Animal()

print(bingo.legs)
print(bingo.habitat)
# print(f"Animal sound: {lion.make_sound()}")
# print(f"Dog sound: {bingo.make_sound()}")
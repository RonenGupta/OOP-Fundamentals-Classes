class Animal:
    def __init__(self):
        self.sound = ""

    def make_sound(self):
        if self.sound == "woof":
            print("Dog goes woof")
        elif self.sound == "meow":
            print("Cat goes meow")
        elif self.sound == "moo":
            print("Cow goes moo")
        else:
            print("Unknown animal sound")

class Dog(Animal):
    def __init__(self):
        self.sound = "woof"

class Cat(Animal):
    def __init__(self):
        self.sound = "meow"

class Cow(Animal):
    def __init__(self):
        self.sound = "moo"


animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.make_sound()

# optimised

class Animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print("Unknown animal sound")

class Dog(Animal):
    def __init__(self):
        self.sound = "woof"

    def make_sound(self):
        print(f"Dog goes {self.sound}")

class Cat(Animal):
    def __init__(self):
        self.sound = "meow"

    def make_sound(self):
        print(f"Cat goes {self.sound}")

class Cow(Animal):
    def __init__(self):
        self.sound = "moo"
        
    def make_sound(self):
        print(f"Cow goes {self.sound}")

animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.make_sound()

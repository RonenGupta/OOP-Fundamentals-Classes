class Animal:
    def __init__(self, _name):
        self._name = _name
    
    def get_sound():

        print("Undefined")

class Dog(Animal):
    def __init__(self, _name, _sound):
        super().__init__(_name)
        self._sound = _sound

    def get_sound(self):
        print(f"Hello, I am a {self._name} and I say {self._sound}.")

class Cat(Dog):
  pass

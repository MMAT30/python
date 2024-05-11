from animal import Animal
from breed import Breed


class Cat(Animal):
    
    def __init__(self, name):
        super().__init__(name, Breed.CAT)
    
    def __str__(self):
        return f"{self.name} is a {self.species.name}"
   
    def speak(self):
        print(f"[+] {self.species.name}: {self.name} says meow")
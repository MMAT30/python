from abc import ABC, abstractmethod


class Animal(ABC):
    
    @abstractmethod
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    @abstractmethod
    def __str__(self):
        
        return f"{self.name} is a {self.species.name}"
    
    @abstractmethod
    def speak(self):
        print(f"{self.name} says something")
    
    
    
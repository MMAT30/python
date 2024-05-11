
from animal import Animal


# polymorphism
def isAnimal(animal: Animal) -> bool:
    
    if isinstance(animal, Animal):
        print(f"[+] {animal.name} is an {animal.species.name}")
        return True
    else:
        print(f"[-] {animal.name} is not an animal")
        return False

from dog import Dog
from cat import Cat
from bird import Bird
from breed import Breed
from isAnimal import isAnimal


def main():
   
    # dog inherits from animal abstract class
    dog = Dog("Buddy")
    print(f"[+] DOG: {dog}")
    dog.speak()
    isAnimal(dog)
    
    # dog inherits from animal abstract class
    cat = Cat("Whiskers")
    print(f"[+] CAT: {cat}")
    cat.speak()
    isAnimal(cat)
    
    # bird inherits from animal abstract class
    bird = Bird("Tweety")
    print(f"[+] BIRD: {bird}")
    bird.speak()
    isAnimal(bird)
    
    


if __name__ == "__main__":
    main()
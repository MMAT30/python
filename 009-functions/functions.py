from typing import List, Dict, Tuple




def main():
    
    print("[+] FUNCTIONS")
    
    f1()
    f2()
    
    # unpacking values from multiple return function
    x, y = f3()
    print(f"[+] f3: {x} {y}")
    
    # unpacking from multiple return function
    x = f4()
    y = [*x, *x] 
    print(f"[+] f4: {y}")
    
    # unpacking values from dictionary
    x = f5()
    y= {
        **x,
        **x["nested_dict"]
    }
    print(f"[+] f5: {y}")
    
    
    x = f6(10, 20)
    print(f"[+] f6: {x}")
    
    
    x = f7(1, 2, 3, 4, 5)
    print(f"[+] f7: {x}")
    
    x = f8(name="John", age=30)
    print(f"[+] f8: {x}")
    
    x = f9()
    print(f"[+] f9: {x}")
    
    x = f10(10)
    print(f"[+] f10: {x}")
    
    x = f12()
    print(f"[+] f12: {x()}")
    print(f"[+] f12: {x()}")
    print(f"[+] f12: {x()}")
    
    
    
    
    
    print("[+] END FUNCTIONS")



def f1() -> None:
    print("[+] FUNCTION 1")


# value returning function
def f2() -> int:
    return 10

# multiple returning function
def f3() -> Tuple[int, str]:

    return 10, "Hello"


# multiple returning function
def f4() -> List[int]:
    return [1, 2, 3, 4, 5]

# dict returning function
def f5() -> Dict:
    return {
        "name": "John",
        "age": 30,
        "nested_dict": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    
    
# argument passing function
def f6(x: int, y: int) -> int:
    return x + y


# any number of positional arguements of same type
def f7(*args: int) -> int:
    return sum(args)


# any number of keyword arguments
def f8(**kwargs) -> Dict:
    return kwargs

# default arguments
def f9(x: int = 10) -> int:
    return x

# lambda function
f10 = lambda x: x + 10

# decorator function
def f11(func):
    def wrapper(*args, **kwargs):
        print("[+] WRAPPER")
        return func(*args, **kwargs)

    return wrapper

# closure with scope of outer function
@f11
def f12():
    # counter that is scoped to only this function
    counter = 0
    
    def increment():
        nonlocal counter
        counter += 1
        return counter
    
    return increment



    

if __name__ == '__main__':
    main()
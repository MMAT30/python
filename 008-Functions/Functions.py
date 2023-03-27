import inspect
from inspect import isfunction, ismethod, isroutine
from functools import wraps



def main():
    
    f1(1,2)
    f2(1)
    f3(1,2)
    f4(1,2,3,4,5,6,7)
    f5(1,2,3,4,5,6,arg5=7)
    f6(-1,0,-7,-6,-5,a=1,b=2,c=3)



    # doc string used with help
    help(f7)
    print(f7.__doc__)
    print(f7.__annotations__, "\n")



    # lambda functions
    f8 = lambda x, y : x + y
    print(f8(1,2), "\n")



    # callable
    print(callable(f1), "\n")



    # function methods
    print(dir(f7))
    print(f7.__doc__)
    print(f7.__annotations__)
    print(f7.__name__)
    print(f7.__defaults__)
    print(f7.__code__.co_name)
    print(f7.__code__.co_varnames)
    print(f7.__code__.co_argcount, "\n")



    # inspect module
    print(isfunction(f7))
    print(ismethod(f7))
    print(isroutine(f7))
    print(inspect.getsource(f7))
    print(inspect.getmodule(f7))
    print(inspect.getmodule(print))
    print(inspect.getcomments(f7))
    print(inspect.signature(f7))



    # function signiture
    sig = inspect.signature(f7)
    
    for x in sig.parameters.values():
        print("name:", x.name)
        print("default:", x.default)
        print("annotation:", x.annotation)
        print("kind:", x.kind)
        print("-" * 40)



    # closure
    c = f9()
    print(c())
    print(c())
    print(c())


    # decorator
    help(adder)
    print(adder(1,1))
    print(adder(1,2))

    # parameterized decorator
    help(subber)
    print(subber(1,1))
    print(subber(2,1))
    print(subber(3,1)) # reached max count of 2
    print(subber(4,1))



    # map - maps  function to data
    data = [1,2,3,4,5] 
    print(data)
    f = lambda x: x * 2
    data = map(f, data)
    print(list(data))


    # filter - filters data based on a function
    data = [1,2,3,4,5,6]
    print(data)
    f = lambda x: x if x % 2 == 0 else False
    data = filter(f, data)
    print(list(data))

    # zip - maps two data structures into one
    d1 = [1,2,3,4,5]
    d2 = ["one", "two", "three", "four", "five"]
    data = zip(d1, d2)
    print(set(data))








# positional arguments
def f1(arg1, arg2):
    print(f"f1({arg1}, {arg2})")


# keyword/default arguments
def f2(arg1, arg2=2):
    print(f"f2({arg1}, {arg2})")

# positional mixed with keyword/default arguments
def f3(arg1, arg2, arg3=3, arg4=4):
    print(f"f3({arg1}, {arg2}, {arg3}, {arg4})")

# *args - unnubered arguments
def f4(arg1, arg2, arg3, *arg4):
    print(f"f4({arg1}, {arg2}, {arg3}, {arg4})")


# *args - unnumbered arguments with positional args
def f5(arg1, arg2, arg3, *arg4, arg5):
    print(f"f5({arg1}, {arg2}, {arg3}, {arg4}, {arg5})")





# **kwargs - unnumbered keyword arguments
def f6(**kwargs):
    print(f"f6({kwargs})")

def f6(arg1, arg2 ,**kwargs):
    print(f"f6({arg1}, {arg2}, {kwargs})")

def f6(arg1, arg2 , *args, **kwargs):
    print(f"f6({arg1}, {arg2}, {args}, {kwargs})")






# doc string and annotations used with help
def f7(arg1: int = 0, arg2: int = 1) -> int:

    """
    returns the sums of arg1 and arg2
    """
    # this is a comment
    return arg1 + arg2


# closure
def f9():
    total = 0
    def add():
        nonlocal total
        total = total + 1
        return total
    return add


# decorator
def counter1(fn):
    cnt = 0

    @wraps(fn)
    def inner(*args, **kwargs):

        """this is the inner function"""

        nonlocal cnt
        cnt = cnt + 1
        print(f"function {fn.__name__} was called {cnt} times")
        return fn(*args, **kwargs)
    return inner





def counter2(max: int = 100):
    def counter(fn):
        """this is the counter function"""
        cnt = 0

        @wraps(fn)
        def inner(*args, **kwargs):

            """this is the inner function"""

            nonlocal cnt
            if cnt < max:
                cnt = cnt + 1
            print(f"function {fn.__name__} was called {cnt} times")
            return fn(*args, **kwargs)
        return inner
    return counter



@counter1
def adder(arg1: int, arg2: int) -> int:
    """adds two numbers and returns the sum"""
    return arg1 + arg2

@counter2(max=2)
def subber(arg1: int, arg2: int) -> int:
    """subs two numbers and returns the sum"""
    return arg1 - arg2





if __name__ == "__main__":
    main()
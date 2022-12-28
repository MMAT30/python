


def main():
    
    # declaring int variable
    n = 777
    print("int value:\t\t", n)
    print("int type:\t\t", type(n), "\n")
    
    
    
    # casting
    print(int("123"))
    print(int(-123.123))
    print(int(True))
    
    
    # casting with bases
    print(int("123", base=10))
    print(int("1010101010", base=2))
    print(int("A2f", base=16), "\n")
    
    
    # alternative formats
    print("num value:\t\t", n)
    print("num bin value:\t\t", bin(n))
    print("num oct value:\t\t", oct(n))
    print("num hex value:\t\t", hex(n))
    
    


    
    
if __name__ == "__main__":
    main()


def main():
    
    # declaring booleans
    b1 = False
    b2 = True
    print(b1, b2, "\n")

    # casting boolean from int
    print(bool(0), bool(1), bool(-1), bool(100), "\n")


    # short circuiting - will check first True and doesnt evaluate the right hand side
    print(True or (False and False and False and False))


    # logical operations
    print(True or True) 
    print(True and True) 
    print(not True) 


    # comparison operations
    print(True == True)
    print(True != True)
    print(True > True)
    print(True < True)
    print(True >= True)
    print(True <= True)


    
    
    
if __name__ == "__main__":
    main()
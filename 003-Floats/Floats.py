from fractions import Fraction



def main():
    
    # declaring floats
    f1 = 0.123
    f2 = 1.234
    print(f1, f2, "\n")
    
    # casting ints and fractions to floats
    print(float(Fraction(1,2)))
    print(float(10), "\n")
    
    
    # formating with f-strings
    print(f"{f1:.25f}\n")
    
    
    
if __name__ == "__main__":
    main()
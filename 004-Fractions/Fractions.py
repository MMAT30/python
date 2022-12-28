import math
from fractions import Fraction


def main():
    
    # declaring fraction
    f1 = Fraction(numerator=1, denominator=2)
    f2 = Fraction(numerator=2, denominator=8)
    print(f1, f2, "\n")
    
    
    # getting only fraction part
    print(f1.numerator, f1.denominator, "\n")


    # casting to a fraction
    print(Fraction("1/8"))
    print(Fraction("0.125"))
    print(Fraction(0.125), "\n")
    
    
    # casting to float
    print(float(f1), type(float(f1)), "\n")
    
    
    # arithmetic operations with fractions
    print(f1 + f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1 ** f2)
    print(f1 + f2)
    print(f1 + f2, "\n")
    
    
    # irrational numbers as fractions
    print(Fraction(math.sqrt(2)))
    
    
    
if __name__ == "__main__":
    main()
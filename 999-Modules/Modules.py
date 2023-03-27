import math

def main():

    # looking a global data
    print(globals())
    print(globals()["math"])

    # type of import
    print(type(math))


if __name__ == "__main__":
    main()
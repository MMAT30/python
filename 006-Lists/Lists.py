
def main():

    # declaring lists
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10]

    # unpacking a list
    a, b, c, d, e = l1
    print(a, b, c, d, e)

    # extended unpacking
    a, *b = l1
    print(a, b)

    a, *b, c, d = l1
    print(a, b, c, d)


    # extended unpacking by skipping
    a, *_, c, d = l1
    print(a, c ,d)

    # list comprehensions
    # data = [x if ]

if __name__ == "__main__":
    main()
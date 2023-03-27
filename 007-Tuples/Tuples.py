

def main():

    # declaring a tuple
    t1 = (1,2,3,4,5,6)
    t2 = (7,8,9,10,11,12)
    print(t1, t2)

    # type of tuple
    print(type(t1))


    # accessing tuple
    print(t1[0])

    # accessing by slice
    print(t1[:3])
    print(t1[3:])

    # reverse slice
    print(t1[::-1])




if __name__ == "__main__":
    main()
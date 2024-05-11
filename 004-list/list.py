



def main():
    print("[+] LIST")
    
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]
    
    # list comprehension
    z = [i for i in x if i % 2 == 0]
    print(f"[+] LIST COMPREHENSION: {z}")
    
    # append
    x.append(6)
    print(f"[+] APPEND: {x}")
    
    # extend
    x.extend(y)
    print(f"[+] EXTEND: {x}")
    
    # insert
    x.insert(0, 0)
    print(f"[+] INSERT: {x}")
    
    # remove
    x.remove(0)
    print(f"[+] REMOVE: {x}")
    
    # pop
    x.pop()
    print(f"[+] POP: {x}")
    
    # index
    print(f"[+] INDEX: {x.index(1)}")
    
    # count
    print(f"[+] COUNT: {x.count(1)}")
    
    # sort
    x.sort()
    print(f"[+] SORT: {x}")
    
    # reverse
    x.reverse()
    print(f"[+] REVERSE: {x}")
    
    # copy
    z = x.copy()
    print(f"[+] COPY: {z}")
    
    # slice
    print(f"[+] SLICE: {x[0:3]}")
    
    # unpack
    a, b, c, d, e = x
    print(f"[+] UNPACK: {a} {b} {c} {d} {e}")
    
    # clear
    x.clear()
    print(f"[+] CLEAR: {x}")

    
    
    print("[+] END LIST")

if __name__ == "__main__":
    main()
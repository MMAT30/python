

def main():
    print("[+] TUPLES")
    
    x = (1, 2, 3, 4, 5)
    
    # index
    print(f"[+] INDEX: {x.index(1)}")
    
    # count
    print(f"[+] COUNT: {x.count(1)}")
    
    # slice
    print(f"[+] SLICE: {x[0:3]}")
    
    # unpack
    a, b, c, d, e = x
    
    print(f"[+] UNPACK: {a} {b} {c} {d} {e}")
    
    # convert to list
    z = list(x)
    print(f"[+] CONVERT TO LIST: {z}")
    
    
    print("[+] END TUPLES")
    
if __name__ == "__main__":
    main()
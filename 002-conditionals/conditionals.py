


def main():
    print("[+] CONDITIONALS")
    
    x = 10
    y = 20
    z = False
    
    
    # if - elif - else
    if x < y:
        print("[+] x < y")
    elif x > y:
        print("[+] x > y")
    else:
        print("[+] x == y")
        
    # ternary operator
    print("[+] x < y") if x < y else print("[+] x >= y")
    
    
    
   
    print("[+] END CONDITIONALS")
    
if __name__ == "__main__":
    main()
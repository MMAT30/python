

def main():
    print("[+] SETS")
    
  
    x = set([1, 2, 3, 4, 5])
    
    
    # add
    x.add(6)
    print(f"[+] ADD: {x}")
    
    # update
    x.update([7, 8, 9, 10])
    print(f"[+] UPDATE: {x}")
    
    # remove
    x.remove(10)
    print(f"[+] REMOVE: {x}")
    
    # discard
    x.discard(9)
    print(f"[+] DISCARD: {x}")
   
    # pop
    x.pop()
    print(f"[+] POP: {x}")
    
    # copy
    z = x.copy()
    print(f"[+] COPY: {z}")
    
    # clear
    x.clear()
    print(f"[+] CLEAR: {x}")
   
    
     
    
    print("[+] END SETS")
    
if __name__ == "__main__":
    main()
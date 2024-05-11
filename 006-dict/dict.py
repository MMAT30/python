
def main():
    print("[+] DICT")
    
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    # keys
    print(f"[+] KEYS: {x.keys()}")
    
    # values
    print(f"[+] VALUES: {x.values()}")
    
    # items
    print(f"[+] ITEMS: {x.items()}")
    
    # get
    print(f"[+] GET: {x.get('name')}")
    
    # pop
    print(f"[+] POP: {x.pop('name')}")
    
    # popitem
    print(f"[+] POPITEM: {x.popitem()}")
    
    # update
    x.update({"name": "John"})
    print(f"[+] UPDATE: {x}")
    
    # decompose
    name, age, city = x.values()
    print(f"[+] DECOMPOSE: {name} {age} {city}")
    
    # copy
    z = x.copy()
    print(f"[+] COPY: {z}")
    
    # clear
    x.clear()
   
    
    print("[+] END DICT")
    
if __name__ == "__main__":
    main()
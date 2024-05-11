from enum import Enum
def main():
    
    print("[+] ENUMS")
    
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
        
    print(f"[+] RED: {Color.RED}")
    print(f"[+] GREEN: {Color.GREEN}")
    print(f"[+] BLUE: {Color.BLUE}")
    
    # retrieve
    print(f"[+] RETRIEVE: {Color(2)}")
    
    
    # iterate
    for color in Color:
        print(f"[+] COLOR: {color}")
        
    # convert to list
    colors = list(Color)
    print(f"[+] CONVERT TO LIST: {colors}")
        
    print("[+] END ENUMS")


if __name__ == "__main__":
    main()
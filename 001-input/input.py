import sys


def main():
    print("[+] INPUT")
    
    for index in range(len(sys.argv)):
        print(f"[+] VAL {index}: {sys.argv[index]}")
        
    print("[+] END INPUT")
    
if __name__ == "__main__":
    main()
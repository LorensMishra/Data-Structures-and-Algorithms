import sys

def solve():
    n = int(sys.stdin.readline().strip())
    
    if n <= 1:
        print("Not Prime")
        return
    
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    
    print("Prime")

if __name__ == "__main__":
    solve()
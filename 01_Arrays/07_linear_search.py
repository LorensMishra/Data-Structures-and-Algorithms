import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    x = int(sys.stdin.readline().strip())
    
    for i in range(n):
        if arr[i] == x:
            print(i)
            return
    
    print(-1)

if __name__ == "__main__":
    solve()
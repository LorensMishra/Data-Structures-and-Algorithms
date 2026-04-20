import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(n-1,-1,-1):
        print(arr[i], end = " ")

if __name__ == "__main__":
    solve()
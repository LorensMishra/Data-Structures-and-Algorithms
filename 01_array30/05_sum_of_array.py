import sys
def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    total = 0
    for i in arr:
        total+=i
    print(total)
if __name__=="__main__":
    solve()
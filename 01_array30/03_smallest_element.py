import sys
def solve():
    n=int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    minimum = arr[0]
    for i in range(1,n):
        if arr[i]<minimum:
            minimum = arr[i]
    print(minimum)
if __name__=="__main__":
    solve()
 
    
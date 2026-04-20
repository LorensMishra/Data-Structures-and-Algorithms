import sys
def solve():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    x = int(sys.stdin.readline().strip())
    left =0
    right = n-1
    while left<= right:
        mid = (left+right)//2
        if arr[mid]==x:
            print(mid)
            return 
        elif arr[mid]<x:
            left = mid+1
        else:
            right = mid -1
    print(-1)
if __name__=="__main__":
    solve()
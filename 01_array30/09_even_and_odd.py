import sys
def solve():
    n=int(sys.stdin.readline().strip())
    arr=list(map(int,sys.stdin.readline().split()))
    even,odd=0,0
    for i in range(n):
        if arr[i]%2==0:
            even+=1
        else:
            odd+=1
    print(even,odd)
    return
if __name__=="__main__":
    solve()            
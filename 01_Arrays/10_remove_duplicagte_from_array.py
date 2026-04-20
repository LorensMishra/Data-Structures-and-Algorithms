import sys
def solve():
    n=int(sys.stdin.readline().strip())
    arr = list(map(int,sys.stdin.readline().split()))
    listcoll =[]
    for i in range(n):
        if arr[i] not in listcoll:
            listcoll.append(arr[i])
    print(listcoll)
if __name__=="__main__":
    solve()
            
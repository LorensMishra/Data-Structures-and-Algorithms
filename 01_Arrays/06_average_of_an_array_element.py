import sys
def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int,sys.stdin.readline().split()))
    total = 0
    add_all=0
    for i in arr:
        total+=1
    for i in arr:
        add_all+=i
    print(add_all/total)
if __name__=="__main__":
    solve()
        
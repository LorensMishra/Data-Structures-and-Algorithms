import sys
def solve():
    n=int(sys.stdin.readline().strip())
    reverse =0
    while n>0:
        digit=n%10
        reverse=(reverse*10)+digit
        n//=10
    print(reverse)
    
if __name__=="__main__":
    solve()
    
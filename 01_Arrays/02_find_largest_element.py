import sys 
def solve():
    n= int(sys.stdin.readline().strip())
    arr = list(map(int,sys.stdin.readline().split()))
    largest = arr[0]
    for i in range(1,n):
        if arr[i]>largest:
            largest = arr[i]
    print(largest)
if __name__ == "__main__":
    solve()
import sys

def solve(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, arr[i]
    return -1

def main():
    arr = list(map(int, sys.stdin.readline().split()))
    
    target_line = sys.stdin.readline().strip()
    
    if not target_line:   #
        print("no target given")
        return

    target = int(target_line)
    print(solve(arr, target))

if __name__ == "__main__":
    main()
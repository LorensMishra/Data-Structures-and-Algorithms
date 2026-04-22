import sys

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def main():
    arr = list(map(int, sys.stdin.readline().split()))
    
    target_line = sys.stdin.readline().strip()
    if not target_line:
        print("target not given")
        return

    target = int(target_line)
    print(binary_search(arr, target))

if __name__ == "__main__":
    main()
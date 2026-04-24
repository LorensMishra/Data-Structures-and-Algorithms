import sys

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def main():
    arr = list(map(int, sys.stdin.readline().split()))
    print(selection_sort(arr))

if __name__ == "__main__":
    main()
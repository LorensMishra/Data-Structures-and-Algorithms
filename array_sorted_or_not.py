n = int(input("Enter a number of elements: "))
arr = list(map(int,input("Enter a number seperated by space: ").split()))
is_sorted = True
for i in range(n-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break
print("Array sorted" if is_sorted else "Not Sorted")
    
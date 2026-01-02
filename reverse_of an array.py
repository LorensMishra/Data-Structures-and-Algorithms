# Reverse of an array using two pointers
# take a input how many numbers in your array list
n = int(input("Enter no of elements : "))

# take array list input
arr = list(map(int, input("Enter numbers seperated by space: ").split()))

left = 0
right = n-1
while left < right:
    arr[left], arr[right]= arr[right], arr[left]
    
    left += 1
    right -= 1
print("Reversed of an array: ", arr)    
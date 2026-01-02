n =  int(input("Enter number : "))
arr = list(map(int, input("Enter numbers seperated by space: ").split()))

largest = second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest 
        largest = num
    elif num != largest and num > second_largest:
        second_largest = num
        
print("Second largest number: ", second_largest)
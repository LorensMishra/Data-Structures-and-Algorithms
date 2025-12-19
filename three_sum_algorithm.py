def three_sum(arr, target):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:  # skip duplicates
            continue

        left = i + 1
        right = n - 1

        while left < right:
            s = arr[i] + arr[left] + arr[right]

            if s == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif s < target:
                left += 1
            else:
                right -= 1

    return result

# Runtime input
n = int(input("Enter number of elements: "))
arr = [int(input("Enter element: ")) for _ in range(n)]
target = int(input("Enter target sum: "))

print("3-Sum result:", three_sum(arr, target))

def product_except_self(nums):
    n = len(nums)  
    if n == 0:
        return []
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result
print(product_except_self([1, 2, 3, 4]))        # [24, 12, 8, 6]
print(product_except_self([2, 3, 4, 5]))        # [60, 40, 30, 24]
print(product_except_self([1, 1, 1, 1]))        # [1, 1, 1, 1]
print(product_except_self([5]))                 # [1]
print(product_except_self([]))                  # []
print(product_except_self([0, 1, 2, 3]))        # [6, 0, 0, 0]
print(product_except_self([1, 2, 0, 4]))        # [0, 0, 8, 0]
print(product_except_self([0, 0, 2, 3]))        # [0, 0, 0, 0]
print(product_except_self([-1, 2, -3, 4]))      # [-24, 12, -8, 6]
print(product_except_self([10, -2, 3, 0]))      # [0, 0, 0, -60]
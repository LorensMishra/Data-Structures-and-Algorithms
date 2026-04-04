def max_product_subarray(nums):
    if not nums:
        return 0
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)
    return result
# 10 Test Cases
print(max_product_subarray([2, 3, -2, 4]))        # 6
print(max_product_subarray([-2, 0, -1]))          # 0
print(max_product_subarray([-2, 3, -4]))          # 24
print(max_product_subarray([0, 2]))               # 2
print(max_product_subarray([-2]))                 # -2
print(max_product_subarray([2, -5, -2, -4, 3]))   # 24
print(max_product_subarray([1, 2, 3, 4]))         # 24
print(max_product_subarray([-1, -3, -10, 0, 60])) # 60
print(max_product_subarray([-2, -3, 0, -2, -40])) # 80
print(max_product_subarray([0, 0, 0]))            # 0
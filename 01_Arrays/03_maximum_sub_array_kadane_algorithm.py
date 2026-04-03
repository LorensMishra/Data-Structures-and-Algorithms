# time Complexity O(n)
# Space Complexity O(1)
def max_subarray(nums):
    if not nums:   # handle empty array
        return 0  
    current_sum = nums[0]
    max_sum = nums[0]   
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)    
    return max_sum
print(max_subarray([]))                       # 0
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(max_subarray([1,2,3,4]))                # 10
print(max_subarray([-1,-2,-3,-4]))            # -1
print(max_subarray([5]))                      # 5
print(max_subarray([-100,1,2,3]))             # 6
print(max_subarray([100,-1,-2,-3]))           # 100
print(max_subarray([1,-1,1,-1,1,-1]))         # 1
print(max_subarray([0,-3,5,-2,1]))            # 5
print(max_subarray([0,0,0,0]))                # 0
print(max_subarray([3,-2,5,-1,6,-3])) 
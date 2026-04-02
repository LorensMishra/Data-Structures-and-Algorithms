# time and Space Complexity 0(n)
def two_sum(nums, target):
    seen = {}  # value -> index
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i
    return [-1, -1]
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 3], 6))
print(two_sum([-1, -2, -3, -4], -6))
print(two_sum([-1, -2, -3, -4], -6))
print(two_sum([0, 4, 3, 0], 0))
print(two_sum([1, 2, 3], 7))
print(two_sum([2, 5, 5, 11], 10))
print(two_sum([2, 5, 5, 11], 10))
print(two_sum([7, 2, 11, 15], 9))
nums = list(range(100000))
print(two_sum(nums, 199998))
nums = list(range(100000))
print(two_sum(nums, 199997))
print(two_sum([5], 5))
print(two_sum([1, 2, 3, 4, 5], 6))
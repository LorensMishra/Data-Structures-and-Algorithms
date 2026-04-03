# Time Complexity O(n)
# Space Complexity O(n)
def contains_duplicate(nums):
    seen = set()   
    for num in nums:
        if num in seen:
            return True
        seen.add(num)  
    return False
print(contains_duplicate([1,2,3,1]))      # True
print(contains_duplicate([1,2,3,4]))      # False
print(contains_duplicate([1,1,1,1]))      # True
print(contains_duplicate([5,6,7,8,5]))    # True
print(contains_duplicate([]))             # False
print(contains_duplicate([10]))           # False
print(contains_duplicate([0,0]))          # True
print(contains_duplicate([-1,-2,-3,-1]))  # True
print(contains_duplicate([2,3,4,5,6]))    # False
print(contains_duplicate([9,8,7,6,5,9]))  # True
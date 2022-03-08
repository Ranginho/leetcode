# simpliest solution:
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)

# more algorithmic solution:
def containsDuplicate(self, nums: List[int]) -> bool:
    value_dict = {}
    for elem in nums:
        if elem in value_dict:
            return True
        else:
            value_dict[elem] = 1
    return False

# with O(1) space:
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False
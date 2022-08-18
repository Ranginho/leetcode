# O(n) solution
def findMin(self, nums: List[int]) -> int:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return nums[i+1]
    return nums[0]

# log(n) solution:
def findMin(self, nums: List[int]) -> int:
    while len(nums) > 2:
        mid_pos = len(nums)//2
        mid_elem = nums[mid_pos]
        left_elem = nums[0]
        right_elem = nums[len(nums)-1]
        if mid_elem > left_elem and mid_elem < right_elem:
            return nums[0]
        elif mid_elem > left_elem and mid_elem >= right_elem:
            nums = nums[mid_pos:]
        elif mid_elem < left_elem:
            nums = nums[0:mid_pos+1]
    if len(nums)==1:
        return nums[0]
    else:
        return min(nums[0], nums[1])
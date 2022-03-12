# O(n^2) solution
def maxSubArray(self, nums: List[int]) -> int:
    if len(nums)==1:
        return nums[0]
    res = -1000000
    for i in range(1, len(nums)+1):
        curr_length = i
        curr_max = -1000000
        for j in range(0, len(nums)-curr_length+1):
            curr_arr = nums[j:j+curr_length]
            if curr_max < sum(curr_arr):
                curr_max = sum(curr_arr)
        if curr_max > res:
            res = curr_max
    return res

# O(n) solution
def maxSubArray(self, nums: List[int]) -> int:
    max_sum, curr_sum = nums[0], nums[0]
    for i in range(1, len(nums)):
        curr_value = nums[i]
        curr_sum += curr_value
        curr_sum = max(curr_value, curr_sum)
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum
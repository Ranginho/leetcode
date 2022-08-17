# O(n^2) solution
def maxSubArray(self, nums: List[int]) -> int:
    starting_pos = 0
    res = nums[0]
    while(starting_pos < len(nums)):
        curr_max = nums[starting_pos]
        curr_sum = nums[starting_pos]
        curr_list = nums[starting_pos+1:]
        for elem in curr_list:
            curr_sum += elem
            if curr_sum > curr_max:
                curr_max = curr_sum
        if curr_max > res:
            res = curr_max
        starting_pos += 1
    return res

# O(n) time complexity solution with O(n) space complexity
def maxSubArray(self, nums: List[int]) -> int:
  res_arr = []
  res_arr.append(nums[0])
  for i, elem in enumerate(nums):
    if i == 0:
      continue
    if res_arr[i-1] > 0:
      res_arr.append(res_arr[i-1] + elem)
    else:
      res_arr.append(elem)
  return max(res_arr)

# O(n) time complexity solution with O(1) space complexity
def maxSubArray(self, nums: List[int]) -> int:
    for i, elem in enumerate(nums):
    if i == 0:
      continue
    if nums[i-1] > 0:
      nums[i] = nums[i-1] + elem
  return max(nums)
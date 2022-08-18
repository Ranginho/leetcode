def threeSum(nums):
    nums.sort()
    res = []
    for i, elem in enumerate(nums):
        curr_target = 0 - elem
        left_ptr = i+1
        right_ptr = len(nums) - 1
        if i > 0 and elem == nums[i-1]:
            continue
        while left_ptr < right_ptr:
            curr_sum = nums[left_ptr] + nums[right_ptr]
            if curr_sum > curr_target:
                right_ptr -= 1
            elif curr_sum < curr_target:
                left_ptr += 1
            elif curr_sum == curr_target:
                curr_res = [elem, nums[left_ptr], nums[right_ptr]]
                res.append(curr_res)
                left_ptr += 1
                while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                    left_ptr += 1
    return res
                
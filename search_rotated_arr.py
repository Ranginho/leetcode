# log(n) solution
def search(nums, target):
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    if len(nums) == 2:
        if nums[0] == target:
            return 0
        elif nums[1] == target:
            return 1
        else:
            return -1
    
    mid_pos = len(nums) // 2
    left_pos = 0
    right_pos = len(nums) - 1
    while mid_pos > left_pos and mid_pos < right_pos:
        if nums[mid_pos] > nums[left_pos]:
            if target >= nums[left_pos] and target <= nums[mid_pos]:
                right_pos = mid_pos
                mid_pos = (left_pos + right_pos) // 2
            else:
                left_pos = mid_pos
                mid_pos = (left_pos + right_pos) // 2
        else:
            if target >= nums[mid_pos] and target <= nums[right_pos]:
                left_pos = mid_pos
                mid_pos = (left_pos + right_pos) // 2
            else:
                right_pos = mid_pos
                mid_pos = (left_pos + right_pos) // 2
    
    if nums[mid_pos] == target:
        return mid_pos
    elif nums[right_pos] == target:
        return right_pos
    elif nums[left_pos] == target:
        return left_pos
    else:
        return -1
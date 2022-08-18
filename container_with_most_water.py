def maxArea(height):
    left_ptr = 0
    right_ptr = len(height)-1
    res = 0
    while left_ptr < right_ptr:
        curr_max = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
        if curr_max > res:
            res = curr_max
        
        if height[left_ptr] < height[right_ptr]:
            left_ptr += 1
        else:
            right_ptr -= 1
    return res
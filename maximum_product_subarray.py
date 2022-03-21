def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    curr_max = 1
    curr_min = 1
    for elem in nums:
        if elem == 0:
            curr_max = 1
            curr_min = 1
            continue
        tmp = curr_max*elem
        curr_max = max(elem, elem*curr_max, elem*curr_min)
        curr_min = min(elem, tmp, elem*curr_min)
        res = max(res, curr_max)
    return res
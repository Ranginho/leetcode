# I calculated prefix and postfix products and used it to get a final result

def productExceptSelf(self, nums: List[int]) -> List[int]:
    left_prods = [nums[0]]
    right_prods = [nums[len(nums)-1]]
    for i in range(1, len(nums)):
        left_prods.append(nums[i]*left_prods[i-1])
    for i in range(1, len(nums)):
        right_prods.append(nums[len(nums)-1-i]*right_prods[i-1])
    right_prods.reverse()
    res = []
    for i in range(len(nums)):
        left = 0
        right = 0
        if (i-1) < 0:
            left = 1
        else:
            left = left_prods[i-1]
        if (i+1) >= len(nums):
            right = 1
        else:
            right = right_prods[i+1]
        res.append(left*right)
    return res
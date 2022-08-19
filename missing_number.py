def missingNumber(nums):
    for i in range(len(nums)+1):
        if i in nums:
            continue
        else:
            return i


def missingNumber(nums):
    # Sum of n natural number is: Sn = n*(n+1)/2
    nums_sum = len(nums)*(len(nums)+1)/2
    
    real_sum = 0
    for elem in nums:
        real_sum += elem
        
    return int(nums_sum - real_sum)


def missingNumber(nums):
    xor = len(nums)
    for i in range(len(nums)):
        xor ^= nums[i] ^ i
    return xor
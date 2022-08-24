# Recursive Solution

def recursiveClimbStairs(n: int, curr_sum: int, res: int) -> int:
    if curr_sum > n:
        return res
    if curr_sum == n:
        res += 1
        return res
    return recursiveClimbStairs(n, curr_sum + 1, res) + recursiveClimbStairs(n, curr_sum + 2, res)

def climbStairs(n: int) -> int:
    res = 0
    res = recursiveClimbStairs(n, 0, res)
    return res


# Dynamic Programming
def climbStairs(n: int) -> int:
    curr_first = 1
    curr_second = 1
    curr_pos = 2
    while curr_pos <= n:
        curr_tmp = curr_second
        curr_second += curr_first
        curr_first = curr_tmp
        curr_pos += 1
    return curr_second
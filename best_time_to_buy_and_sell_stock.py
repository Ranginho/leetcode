def maxProfit(self, prices: List[int]) -> int:
    left_ptr, right_ptr = 0, 1
    res = 0
    while right_ptr < len(prices):
        if prices[left_ptr] < prices[right_ptr]:
            res = max(res, prices[right_ptr] - prices[left_ptr])
        else:
            left_ptr = right_ptr
        right_ptr += 1
    return res
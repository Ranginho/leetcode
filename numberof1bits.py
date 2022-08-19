def hammingWeight(n):
    num = bin(n).replace("0b", "")
    counter = 0
    for char in num:
        if char == '1':
            counter += 1
    return counter

# time - O(1), space - O(1)
def hammingWeight(n):
res = 0
while n > 0:
    res += n%2
    n = n >> 1
return res

# time - O(1), space - O(1)
def hammingWeight(n):
    res = 0
    while n > 0:
        n = n & (n-1)
        res += 1
    return res
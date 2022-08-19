def countBits(n):
    res = []
    for i in range(n+1):
        if i == 0:
            res.append(0)
        if i == 1:
            res.append(1)
        if i%2 == 1 and i != 0 and i != 1:
            last_elem = res[i//2]
            res.append(last_elem + 1)
        if i%2 == 0 and i != 0 and i != 1:
            res.append(res[i//2])
    return res
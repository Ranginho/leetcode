def topKFrequent(nums, k):
    dictionary = {}
    for elem in nums:
        if elem in dictionary:
            val = dictionary[elem]
            val += 1
            dictionary[elem] = val
        else:
            dictionary[elem] = 1
    
    res = []
    for i in range(k):
        dict_max = max(dictionary, key=dictionary.get)
        res.append(dict_max)
        dictionary[dict_max] = -1
    
    return res


def topKFrequent(nums, k):
    dictionary = {}
    for elem in nums:
        dictionary[elem] = 1+dictionary.get(elem, 0)
    
    arr = [[] for i in range(len(nums)+1)]

    for key, value in dictionary.items():
        arr[value].append(key)
    
    res = []
    for i in range(len(arr)-1, 0, -1):
        for n in arr[i]:
            res.append(n)
            if len(res) == k:
                return res
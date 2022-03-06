def twoSum(self, nums: List[int], target: int) -> List[int]:
    ind1: int = 0
    ind2: int = 0
    val_ind_dict = {}
    for ind, elem in enumerate(nums):
        diff = target - elem
        if diff in val_ind_dict:
            return [ind, val_ind_dict[diff]]
        else:
            val_ind_dict[elem] = ind
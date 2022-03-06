def twoSum(self, nums: List[int], target: int) -> List[int]:
    val_ind_dict = {}
    for ind, elem in enumerate(nums):
        diff = target - elem
        if diff in val_ind_dict:
            return [ind, val_ind_dict[diff]]
        else:
            val_ind_dict[elem] = ind
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        return self.helper(root, arr, k)[k-1]
        
    def helper(self, root, arr, k):
        if root:
            self.helper(root.left, arr, k)
            arr.append(root.val)
            if len(arr) == k:
                return arr
            self.helper(root.right, arr, k)
        return arr
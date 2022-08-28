# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ress = ListNode()
        copy_res = ress
        remembered = 0
        while l1 or l2 or remembered:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            curr_sum = val1 + val2 + remembered
            remembered = curr_sum // 10
            val = curr_sum % 10
            curr_node = ListNode(val)
            ress.next = curr_node
            ress = ress.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return copy_res.next
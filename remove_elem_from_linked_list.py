# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        copy_head = ListNode(None)
        copy_head.next = head
        node = copy_head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return copy_head.next
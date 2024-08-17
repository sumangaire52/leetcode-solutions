# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        node = head
        while node:
            # Shift left by 1 (which is equivalent to multiplying by 2) 
            # and add the current node's value
            decimal = (decimal << 1) | node.val
            node = node.next
        return decimal

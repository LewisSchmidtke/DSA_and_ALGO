# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy = prev = ListNode(0, head)

        while curr:
            if curr.val != val:
                prev = curr
                curr = curr.next
                continue

            while curr and curr.val == val:
                prev.next = curr.next
                curr = curr.next
            
            prev = curr
            if curr:
                curr = curr.next

        return dummy.next
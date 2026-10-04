# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0 
        curr = head
        while (curr != None):
            count += 1
            curr = curr.next  # Added assignment to move the pointer
        
        mid = (count // 2) + 1
        
        # Traverse to the mid-th node
        curr = head
        for _ in range(mid - 1):
            curr = curr.next

        return curr  # Returns the ListNode instance
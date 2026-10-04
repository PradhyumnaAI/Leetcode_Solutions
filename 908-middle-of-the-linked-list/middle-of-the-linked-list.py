

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head 
        fast = head 
        while fast != None and fast.next!= None:
            slow = slow.next
            fast = fast.next.next

        return slow  
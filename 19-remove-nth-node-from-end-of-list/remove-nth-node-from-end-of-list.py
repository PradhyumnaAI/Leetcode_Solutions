class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # 1. Count total nodes
        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next
        
        k = count - n 

        
        if k == 0:
            return head.next

        
        curr = head
        for i in range(k - 1):
            curr = curr.next

        
        curr.next = curr.next.next

        return head
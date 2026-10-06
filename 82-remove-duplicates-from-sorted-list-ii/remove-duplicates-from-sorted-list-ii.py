class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        # Step 1: Remove any duplicates right at the beginning of the list
        while head != None and head.next != None and head.val == head.next.val:
            val = head.val
            while head != None and head.val == val:
                head = head.next

        # If the whole list was made of duplicates, return None
        if head == None:
            return head

        
        prev = head
        curr = head.next

        while curr != None and curr.next != None:
            if curr.val == curr.next.val:
                val = curr.val
                
                while curr != None and curr.val == val:
                    curr = curr.next
                
                prev.next = curr
            else:
                
                prev = curr
                curr = curr.next

        return head
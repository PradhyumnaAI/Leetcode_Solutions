class Solution:
    def deleteDuplicates(self, head: list) -> list:
        curr = head 
        while (curr != None and curr.next != None):
            if head == None: 
                return head 
            if (curr.val == curr.next.val):
                curr.next = curr.next.next
            else : 
                curr = curr.next
        return head 


        
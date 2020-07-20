Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

=========================================
class Solution:
    
# @param {ListNode} head
# @param {integer} val
# @return {ListNode}

    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        
        next = dummy
        
    
        while next != None and next.next != None:
            
            if next.next.val == val:
                
               next.next = next.next.next
            else:
               next = next.next
        
        return dummy.next

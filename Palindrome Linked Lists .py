Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true




=====================================================================================================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        slow , fast =head ,head
        
        stk=[]
        while fast and fast.next:
            stk.append(slow.val)
            slow = slow .next
            fast = fast.next.next
        if fast:
            slow =slow.next
        while(slow and len(stk)):
            if stk.pop() != slow.val:
                return False
            slow = slow.next
        return True    
    
    
        

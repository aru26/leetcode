Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

========================================================================================================================================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr =head
        fastPtr = head.next
        while ptr is not None and fastPtr is not None and fastPtr.next is not None:
            if ptr == fastPtr:
                return True
            ptr = ptr.next
            fastPtr = fastPtr.next.next
        return False   
        
  

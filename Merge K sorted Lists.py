# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.node = []
        dummy  =head = ListNode(0)
        for l in lists:
            while l:
                self.node.append(l.val)
                l = l.next
        for x in sorted (self.node):
            dummy.next = ListNode(x)
            dummy = dummy.next
        return head.next   
                

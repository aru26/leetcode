# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        if len(lists)==1:
            return lists[0]
        mid  =len(lists)//2
        l=self.mergeKLists(lists[:mid])
        r=self.mergeKLists(lists[mid:])
        return self. merge(l,r)
   
    def merge(self , l1,l2):
        curr= dummy =ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next=ListNode(l1.val)
                curr=curr.next
                l1=l1.next
            else:
                curr.next =ListNode(l2.val)
                curr=curr.next
                l2=l2.next
                
        if l1:
            curr.next=l1
        else:
            curr.next=l2
          
        return dummy.next
     ==================================================
    """   
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
        #this  block is naother way to code the problem
        """
    ==============================================
                
    
    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

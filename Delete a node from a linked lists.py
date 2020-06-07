python code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        while node.next.next != None:
            node .val =node.next.val
            node = node.next
        node.val =node.next.val
        node.next = None
        ======================================================================================================
            Java code
            /**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        node .val = node.next.val;
        node .next = node.next.next  ;  
            
    }
}
        
        

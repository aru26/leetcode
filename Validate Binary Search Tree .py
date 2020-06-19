Approach 1: Recursion
The idea above could be implemented as a recursion. One compares the node value with its upper 
and lower limits if they are available. Then one repeats the same step recursively for
left and right subtrees.

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
        
        Complexity Analysis

Time complexity : \mathcal{O}(N)O(N) since we visit each node exactly once.
Space complexity : \mathcal{O}(N)O(N) since we keep up to the entire tree.
=========================================================================================================================
Approach 2: Iteration
The above recursion could be converted into iteration, with the help of stack. 
DFS would be better than BFS since it works faster here.

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True  
        
        Complexity Analysis

Time complexity : \mathcal{O}(N)O(N) since we visit each node exactly once.
Space complexity : \mathcal{O}(N)O(N) since we keep up to the entire tree.
==========================================================================================================================
Approach 3: Inorder traversal
Algorithm

Let's use the order of nodes in the inorder traversal Left -> Node -> Right.

postorder

Here the nodes are enumerated in the order you visit them, and you could follow 1-2-3-4-5 to compare different strategies.

Left -> Node -> Right order of inorder traversal means for BST that each element should be smaller than the next one.

Hence the algorithm with \mathcal{O}(N)O(N) time complexity and \mathcal{O}(N)O(N) space complexity could be simple:

Compute inorder traversal list inorder.

Check if each element in inorder is smaller than the next one.

postorder

Do we need to keep the whole inorder traversal list?

Actually, no. The last added inorder element is enough to ensure at each step that the tree is BST (or not). 
Hence one could merge both steps into one and reduce the used space.


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
        Complexity Analysis

Time complexity : \mathcal{O}(N)O(N) in the worst case when the tree is BST or the "bad" element is a rightmost leaf.

Space complexity : \mathcal{O}(N)O(N) to keep stack.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth
      ============================================================================================================================
      Depth First Search: Iterative Version

Push the root and the level on the stack.
Pop and push left and right kids of root. Update the max_level variable.
Time and Space Complexity: O(N)
class Solution_DFS_Pre_Order(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_level = 0
        self.helper(root, 0)
        return self.max_level
    
    def helper(self, root, level):
        self.max_level = max(self.max_level, level)
        if root:
            self.helper(root.left, level+1)
            self.helper(root.right, level+1)
        return
        
        =========================================================================================================================
        Breadth First Search: Iterative Version

Traverse level by level and keep a counter to track level count
Time and Space Complexity: O(N)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        st, max_level = [], 0
        if root:
            st.append((root, 1))
        while st:
            x, level = st.pop()
            max_level = max(max_level, level)
            if x.left:
                st.append((x.left, level+1))
            if x.right:
                st.append((x.right, level+1))
        return max_level

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level, direction = [], [root], 1
        while level:
            res.append([n.val for n in level][::direction])
            direction *= -1
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

==============================================================================================================================================
#We use stack to do dfs and also keep backtrack state to remove coordinates.
#The idea is that after we visit a node, we add a backtracking node to remove the node if we ever come back to the current stack level.
class Solution(object):
    def neighbors(self, board, r, c):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        nbs = []
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if (0 <= nr < len(board)) and (0 <= nc < len(board[nr])):
                nbs.append((nr, nc))
        return nbs
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        q = list()
				
        for r in range(len(board)): # find starting points
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    q.append((r, c))
                    
        for (r, c) in q:
            visited = set()
            stack = list()
            stack.append((r, c, 0, False)) # regular forward moving node
            while stack:
                cr, cc, i, backtrack = stack.pop()
                if backtrack:
                    visited.remove((cr, cc))
                    continue
                    
                visited.add((cr, cc))
                stack.append((cr, cc, i, True)) # add backtracking node
                if i == (len(word) - 1):
                    return True
            
                for nr, nc in self.neighbors(board, cr, cc):
                    if (nr, nc) in visited:
                        continue
                    if board[nr][nc] == word[i + 1]:
                        stack.append((nr, nc, i + 1, False)) # forward-moving node
            
        return False
=======================================================================================================================================

def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False
        












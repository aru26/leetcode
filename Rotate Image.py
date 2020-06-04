method 1:

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        matrix.reverse()
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(nrow):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
   
   
  method 2 :
  class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        for row in range(n):
            for col in range(row,n):
                matrix[col][row], matrix[row][col]= matrix[row][col], matrix[col],[row]
                
        for i in range(n):
            matrix[i].reverse()

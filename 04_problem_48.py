class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row to get the rotated matrix
        for i in range(n):
            matrix[i].reverse()
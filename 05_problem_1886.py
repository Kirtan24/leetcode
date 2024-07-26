class Solution(object):
    def findRotation(self, mat, target):
        flg = False
        for _ in range(4):
            mat = self.rotate(mat)
            flg = (mat == target)
            if flg:
                return flg
        return flg
    
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

        return matrix
        
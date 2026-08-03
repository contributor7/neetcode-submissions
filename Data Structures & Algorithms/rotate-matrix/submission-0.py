class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # print(matrix)
        matrix.reverse()
        # print(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix [j][i] = matrix[j][i], matrix[i][j]
        
        
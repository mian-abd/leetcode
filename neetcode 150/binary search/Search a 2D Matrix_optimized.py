class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        n = len(matrix[0])
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            m = (l+r) // 2
            row = m // n
            col = m % n
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
        
        return False
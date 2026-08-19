class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        left, right = 0, COLS - 1
        while left <= right:
            value = (left + right) // 2
            if target > matrix[row][value]:
                left = value + 1
            elif target < matrix[row][value]:
                right = value - 1
            else:
                return True
        return False

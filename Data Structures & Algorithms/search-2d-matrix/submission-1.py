class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow = 0 
        rrow = len(matrix) - 1
        correctrow = lrow
        while lrow <= rrow:
            mid = lrow + (rrow - lrow) // 2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[mid]) - 1] >= target:
                correctrow = mid
                break
            elif matrix[mid][0] > target:
                rrow = mid - 1
            else:
                lrow = mid + 1
        left = 0
        right = len(matrix[correctrow]) - 1
        print(right)
        while left <= right:
            m = left + (right - left) // 2
            if matrix[correctrow][m] == target:
                return True
            elif matrix[correctrow][m] > target:
                right = m - 1
            else:
                left = m + 1
        return False
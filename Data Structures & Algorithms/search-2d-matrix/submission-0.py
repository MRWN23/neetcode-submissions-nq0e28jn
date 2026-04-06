class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = math.floor((l+r)/2)

            row = mid // n
            column = mid % n

            if matrix[row][column] > target:
                r = mid - 1
            elif matrix[row][column] < target:
                l = mid + 1
            else:
                return True

        return False


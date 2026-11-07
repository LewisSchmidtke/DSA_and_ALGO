class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid_row = (low + high) // 2

            if matrix[mid_row][0] > target:
                high = mid_row - 1
                continue

            elif matrix[mid_row][-1]  < target:
                low = mid_row + 1
                continue

            current_row: List = matrix[mid_row]
            left: int = 0
            right: int = len(current_row)
            while left <= right:
                mid: int = (right + left) // 2

                if current_row[mid] == target:
                    return True
                
                if current_row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return False
        
        return False

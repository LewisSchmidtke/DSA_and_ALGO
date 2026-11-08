class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        total_value = sum(ribbons)

        if k > total_value:
            return 0
        if k == total_value:
            return 1

        minSize = 0
        maxSize = max(ribbons)

        res = minSize

        while minSize <= maxSize:
            midSize = (minSize + maxSize) // 2
            if self.is_cuttable(midSize, ribbons, k):
                res = max(res, midSize)
                minSize = midSize + 1
            else:
                maxSize = midSize - 1
        
        return res

    def is_cuttable(self, size, arr, threshold):
        total_ribbs = 0
        for ribbon in arr:
            total_ribbs += ribbon // size

            if total_ribbs >= threshold:
                return True
        
        return False





        
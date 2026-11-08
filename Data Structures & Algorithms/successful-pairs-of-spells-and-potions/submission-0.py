class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        total_potions = len(potions)
        potions.sort()

        res = []
        for spell in spells:
            left = 0
            right = total_potions - 1
            min_index = right

            if potions[right] * spell < success:
                res.append(0)
                continue

            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                    min_index = min(min_index, mid)
                else:
                    left = mid + 1
            
            res.append(total_potions - min_index)

        return res
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.days = days

        minW = max(weights)
        maxW = sum(weights)
        res = maxW

        while minW <= maxW:
            capM = (minW + maxW) // 2

            if self.check_capacity(capM):
                res = min(res, capM)
                maxW = capM - 1
            else:
                minW = capM + 1
        
        return res

    def check_capacity(self, capacity):
        cap = capacity
        needed_days = 1

        for w in self.weights:
            if cap - w < 0:
                needed_days += 1
                if needed_days > self.days:
                    return False
                cap = capacity
                
            cap -= w

        return True


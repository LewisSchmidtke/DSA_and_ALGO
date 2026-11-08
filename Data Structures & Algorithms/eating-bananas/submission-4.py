class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.time = h
        self.piles = piles
        self.totalBananas = sum(piles)
        
        minSpeed = 1
        maxSpeed = self.totalBananas

        eatingRate = maxSpeed

        while minSpeed <= maxSpeed:
            midSpeed = (minSpeed + maxSpeed) // 2
            if self.can_eat(midSpeed):
                print(midSpeed)
                eatingRate = min(eatingRate, midSpeed)
                maxSpeed = midSpeed - 1
            else:
                minSpeed = midSpeed + 1
        
        return eatingRate

    def can_eat(self, rate):
        total_time = 0
        for pile in self.piles:
            if rate >= pile:
                time = 1
            else:
                time = pile // rate
                if pile % rate > 0:
                    time += 1

            total_time += time
            if total_time > self.time:
                return False
        return True

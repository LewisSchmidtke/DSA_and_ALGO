class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = bottles = numBottles

        while bottles >= numExchange:
            bottles -= numExchange
            bottles += 1
            total += 1
        
        return total

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        smallestYet = max(prices)
        biggestAfter = 0
        bestDiff = 0

        for i in prices:
            if i < smallestYet:
                smallestYet = i
                biggestAfter = 0
            elif i > biggestAfter:
                biggestAfter = i
                bestDiff = max(bestDiff, biggestAfter - smallestYet)
        
        return bestDiff
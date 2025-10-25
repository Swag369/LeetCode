class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        base_satisfied = 0

        n = len(customers)

        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]
        

        added = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                added += customers[i]

        max_sat = base_satisfied + added

        for i in range(1, n-minutes+1):

            if grumpy[i-1] == 1:
                added -= customers[i-1]

            if grumpy[i+minutes-1] == 1:
                added += customers[i+minutes-1]


            max_sat = max(max_sat, base_satisfied + added)

        return max_sat
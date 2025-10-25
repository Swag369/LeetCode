class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for a in c:
            if c[a]>2:
                return False

        return True
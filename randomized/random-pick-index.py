class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for idx, val in enumerate(nums):
            self.d[val].append(idx)
        print(self.d)

    def pick(self, target: int) -> int:
        # if target not in self.d:
            # return null
        return self.d[target][random.randint(0, len(self.d[target])-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
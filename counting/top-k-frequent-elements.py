import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # print(c)
        a = list(c)
        # print(a)
        a.sort(reverse = True, key=lambda x:c[x])
        # print(a)
        return a[:k]
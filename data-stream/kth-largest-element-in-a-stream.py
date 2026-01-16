import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapq.heapify(self.h)
        self.k = k
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        
        elif self.h[0] < val:
            heapq.heappop(self.h)   
            heapq.heappush(self.h, val)


        return self.h[0]

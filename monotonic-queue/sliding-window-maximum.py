class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        ret = []
        q = []
        q_start = 0

        def add_q(num):
            while(len(q) > q_start and q[-1] < num):
                q.pop()
            q.append(num)

        for i in range(k):
            add_q(nums[i])


        for i in range(1, len(nums) - (k-1)):
            
            # print(i, q_start, q)

            ret.append(q[q_start])

            if nums[i-1] == q[q_start]:
                q_start += 1
            
            add_q(nums[i+k-1])

        ret.append(q[q_start])

        return ret
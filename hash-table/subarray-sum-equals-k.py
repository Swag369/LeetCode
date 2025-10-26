class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        cursum = 0

        prefix = [nums[0]]

        for i in nums[1:]:
            prefix.append(prefix[-1] + i)


        seen_prefixes = dict()

        for i in prefix:
            if i in seen_prefixes:
                seen_prefixes[i] += 1
            else:
                seen_prefixes[i] = 1

            if i == k:
                count += 1
            
            required_removal = (i - k)

            if required_removal in seen_prefixes:
                count += seen_prefixes[required_removal]
            
        
        return count




        
        # prefix[i] = 0...i, prefix[i] - prefix[k] = k+1...i





        # sliding window won't work for negative numbers
        # l = r = 0
        # cur_sum = nums[0]
        # ret = 0

        # while l < len(nums):
            
        #     if cur_sum < k and r < len(nums):
        #         r += 1
        #         cur_sum += nums[r]
            
        #     if cur_sum > k and:
        #         l += 1
        #         cur_sum -= nums[l]
            
        #     if cur_sum == k:
        #         ret += 1
        #         l += 1
            
        # return ret
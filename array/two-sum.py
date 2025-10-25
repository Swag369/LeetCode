class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        i = 0
        for n in nums:
        
            if map.get(n, -1) != -1:
                return [map.get(n, -1), i]
        
            map[target-n] = i

            i+= 1
        print(map)
        
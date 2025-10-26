class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen_i = set()
        smallest_key_triplet_map = dict()

        # print(nums)

        for i in range(len(nums)):

            if i in seen_i:
                continue
            
            mini_total = 0 - nums[i]

            k = len(nums) - 1
            j = i + 1

            while(j < k):
                # print("i,j,k", i, j, k)
                if nums[j] + nums[k] < mini_total:
                    j += 1
                elif nums[j] + nums[k] > mini_total:
                    k -= 1
                else:
                    # print("worked!")
                    if nums[i] in smallest_key_triplet_map:
                        smallest_key_triplet_map[nums[i]].add((nums[i], nums[j], nums[k]))
                    else:
                        smallest_key_triplet_map[nums[i]] = {(nums[i], nums[j], nums[k])}
                        # smallest_key_triplet_map[i].add((nums[i], nums[j], nums[k]))
                    # print(smallest_key_triplet_map)
                    j += 1


        # print(smallest_key_triplet_map)

        ret = []
        for i in smallest_key_triplet_map.keys():
            for j in smallest_key_triplet_map[i]:
                ret.append(j)

        return ret
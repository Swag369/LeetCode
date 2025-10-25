class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # for i in range(nums): #size
        #     for j in range(i): #combinations

        answers = []
        def helper(nums, my_set):

            if len(nums) == 0:
                answers.append(my_set)
                return

            new_set = list(my_set)
            new_set.append(nums[0])

            helper(nums[1:], my_set)
            helper(nums[1:], new_set)
        
        helper(nums, [])

        return answers
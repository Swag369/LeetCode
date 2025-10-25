answers = []
visited = []
cur_set = []

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        global answers, visited, cur_set

        answers = []
        visited = []
        cur_set = []

        for i in nums:
            visited.append(False)

        def helper():
            if len(cur_set) == len(nums):
                answers.append(list(cur_set))
            for k, i in enumerate(nums):
                if visited[k]:
                    continue
                cur_set.append(i)
                visited[k] = True
                helper()
                cur_set.pop()
                visited[k] = False

        helper()

        return answers
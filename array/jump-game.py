class Solution:

    def __init__(self):
        self.dp = [1]

    def canJump(self, nums: List[int]) -> bool:

        if self.dp == [1]:
            self.dp = [False] * len(nums)
            # print("init DP arr")
        # else:
            # print("DP arr alrdy exists")

        if len(nums) == 1:
            return True

        for i_complement in range(len(nums)-1):

            i = len(nums)-2 - i_complement


            # instead of looking at EVERY way, try to go backwards and see if there is ANY way

            #if I can get from partway to end, I just recurse from beginning until THAT point

            if i + nums[i] >= len(nums) - 1 and self.dp[i] == False:

                # print("checking to get to", i, "who has", nums[i], "with end reference of", len(nums) - 1)
                # print(i)

                if self.canJump(nums[:i+1]):
                    return True
                else:
                    self.dp[i] = True

        return False
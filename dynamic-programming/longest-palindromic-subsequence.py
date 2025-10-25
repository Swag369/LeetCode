class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp=t = [[-1]*len(s) for i in range(len(s))]
        i = 0
        j = len(s)-1

        #helper returns len of longest palindromic sunsequence WITHIN i and j inclusive
        def helper(i, j):

            if i==j:
                return 1
            if i>j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            #actually solving longest subseq BETWEEN i and j

            ret = -1

            if s[i] == s[j]:
                ret = 2 + helper(i+1,j-1)
            
            else:
                ret = max(helper(i+1, j), helper(i, j-1))

            dp[i][j] = ret
            return ret


        if len(s) == 1:
            return 1
        else:
            return helper(i,j)

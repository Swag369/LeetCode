class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = []

        def helper(string, stillopen, n):

            # print('looking at', string, stillopen, n)

            if n == 0:
                ret.append(string)
                return

            if stillopen == n:
                string+=")"
                helper(string, stillopen-1, n-1)

            else:
                helper(string+"(", stillopen+1, n-1)
                if stillopen > 0:
                    helper(string+")", stillopen-1, n-1)


        helper("(", 1, n*2-1)




        return ret
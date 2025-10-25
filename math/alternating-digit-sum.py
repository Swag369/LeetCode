class Solution:
    def alternateDigitSum(self, n: int) -> int:
        first_was_positive = True
        ret = 0
        even = True
        while n > 0:
            a = n%10
            if even:
                ret += a
            else:
                ret -= a
            n //=10
            even = not even
        

        if even == True:
            ret *= -1
        
        return ret
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        sol = (len(height)-1)*min(height[l], height[r])

        while l<r:
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            sol = max(sol, (r-l)*min(height[l], height[r]))
            print(sol, (l-r)*min(height[l], height[r]))

        return sol
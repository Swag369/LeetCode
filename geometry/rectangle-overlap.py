class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec1[0],rec1[1],rec1[2],rec1[3] = rec1
        # rec2[0],rec2[1],rec2[2],rec2[3] = rec2

        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False
        # print("a")

        # if rec2[0] <= rec1[0] and rec2[2] >= rec1[2] and rec2[1] <= rec1[1] and rec2[3] >= rec1[3]:
        #     return False
        # print("b")
        
        # if rec2[0] >= rec1[0] and rec2[2] <= rec1[2] and rec2[1] => rec1[1] and rec2[3] <= rec1[3]:
        #     return False
        # print("c")

        return True
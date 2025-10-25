class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1

        ans = False
        idx = 0
        half = True

        while t <= b:
            halfarr = (t+b)//2
            half = matrix[halfarr][0]

            if half < target and matrix[halfarr][-1] < target:
                t = halfarr + 1
            elif half > target and matrix[halfarr][-1] > target:
                b = halfarr - 1
            else:
                half = True
                idx = halfarr
                break

        print(idx)

        if not half:
            return False
        

        print("sec")

        t = 0
        b = len(matrix[idx])-1

        ans = False
        half = True

        while t <= b:
            halfarr = (t+b)//2
            print(halfarr)
            arr = matrix[idx]
            half = arr[halfarr]

            if half < target:
                t = halfarr + 1
            elif half > target:
                b = halfarr - 1
            else:
                return True
        return False
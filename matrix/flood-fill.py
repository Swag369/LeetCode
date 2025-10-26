class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, c: int) -> List[List[int]]:
        
        s = [(sr,sc)]
        oc = image[sr][sc]

        if oc == c:
            return image

        while len(s) > 0:
            print(s)
            i, j = s.pop()
            
            if image[i][j] != oc:
                continue
            
            image[i][j] = c

            if i < len(image)-1:
                s.append((i+1, j))
            if j < len(image[0])-1:
                s.append((i, j+1))
            if i > 0:
                s.append((i-1, j))
            if j > 0:
                s.append((i, j-1))

        return image
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        letters = []
        for c in s:
            if letters == []:
                letters.append([c,1])
            elif letters[-1][0] == c:
                letters[-1][1]+=1
                if letters[-1][1] == k:
                    letters.pop()
            else:
                letters.append([c,1])
        
        ret = ""
        for i in letters:
            for j in range(i[1]):
                ret += i[0]

        return ret
class Solution:
    def findValidPair(self, s: str) -> str:
        
        m = Counter(s)

        for i in range(len(s) - 1):
            # print(int(s[i]), m[s[i]], int(s[i+1]), m[s[i+1]])
            if int(s[i]) == m[s[i]] and int(s[i+1]) == m[s[i+1]] and s[i] != s[i+1]:
                return str(s[i]) + str(s[i+1])
        
        return ""
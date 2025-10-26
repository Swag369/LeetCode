class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # c1= Counter(s1)
        # c2= Counter(s2)
        # prefix_foward = [0 for _ in range(len(s2))]

        # for i in range(len(s2)):
        #     prefix_foward[i] = Counter(s2[:i])

        # prefix_forward.insert(0,Counter(""))

        # window = len(s1)

        # for i in range(window-1, len(s2)):
        #     prefix_forward[]

        # print(c1, c2)
        # print(c2-c1)
    
        if len(s2) < len(s1):
            return False

        c = Counter(s2[:len(s1)])
        cref = Counter(s1)

        for i in range (len(s1) , len(s2)):
            # i is cur letter newly added
            # i - len(s1) is cur letter now removed

            c[s2[i]] += 1
            c[s2[i-len(s1)]] -= 1
            if c[s2[i-len(s1)]] == 0:
                del c[s2[i-len(s1)]]

            # print("comparing", c ,cref, "at", i)

            if c == cref:
                return True
        
        return False
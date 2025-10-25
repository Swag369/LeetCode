class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        m = dict()
        for i in matches:
            w, l = i

            if l in m:
                m[l] += 1
            else:
                m[l] = 1
            if w not in m:
                m[w] = 0

        # print(m)

        ones = []
        zeros = []
        for i in m:
            if m[i] == 0:
                zeros.append(i)
            elif m[i] == 1:
                ones.append(i)
            # print("looking at", i, "got", m[i], "with", len(m[i]))

        zeros.sort()
        ones.sort()

        return [zeros, ones]


        #personal solution, above is from looking at editorial and basing off approach 3
        #only real diff was that he only kept track of count, while I was storing actual losses
        # m = dict()
        # for i in matches:
        #     w, l = i

        #     if l in m:
        #         m[l].append(w)
        #     else:
        #         m[l] = [w]
            
        #     if w not in m:
        #         m[w] = []

        # # print(m)

        # ones = []
        # zeros = []
        # for i in m:
        #     if len(m[i]) == 0:
        #         zeros.append(i)
        #     elif len(m[i]) == 1:
        #         ones.append(i)
        #     # print("looking at", i, "got", m[i], "with", len(m[i]))

        # zeros.sort()
        # ones.sort()

        # return [zeros, ones]
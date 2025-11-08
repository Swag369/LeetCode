class Solution:
    def smallestStringWithSwaps(self, s: str, direct_swaps: List[List[int]]) -> str:

        s = list(s)

        union_find = [i for i in range(len(s))]
        rank = [1 for i in range(len(s))]

        def parent(i):
            path = []

            while union_find[i] != i:
                path.append(i)
                i = union_find[i]

            for idx in path:
                union_find[idx] = i

            return i

        # def parent(i, path=None):
        #     if not path:
        #         path = []
        #     if union_find[i] == i:
        #         for idx in path:
        #             union_find[idx] = i
        #         return i
        #     return parent(union_find[i], path.append(i)) #autocompress

        def check_connected(i, j):
            return parent(i) == parent(j)

        def connect(i, j):
            jp = parent(j)
            ip = parent(i)
            # union_find[jp] = ip
            if rank[jp] < rank[ip]:
                union_find[jp] = ip
                rank[jp] += rank[ip]
            else:
                union_find[ip] = jp
                rank[ip] += rank[jp]

        for i, j in direct_swaps:

            connect(i, j)

        #     if i in swaps:
        #         swaps[i].add(j)
        #     else:
        #         swaps[i] = set([j])

        #     if j in swaps:
        #         swaps[j].add(i)
        #     else:
        #         swaps[j] = set([i])


        #     for k in swaps[i]:
        #         swaps[j].add(k)
        #         swaps[k].add(j)
        #     for k in swaps[j]:
        #         swaps[i].add(k)
        #         swaps[k].add(i)

        # print(union_find)

        # sortable_keys = sorted(swaps.keys())


        # create connected sets
        d = {}
        for i in range(len(union_find)):
            p = parent(i)
            if p in d:
                d[p].add(i)
            else:
                d[p] = set([i])


        # print(d)

        for dsjnt_set in d:

            conns = list(d[dsjnt_set]) # list of idxs in this dsjt set
            letters = list(map(lambda partner_idx: s[partner_idx], conns)) # list of letters in this dsjt set
            conns.sort()
            letters.sort()
            # print(conns)
            # print(letters)

            for j in range(len(conns)):
                s[conns[j]] = letters[j]


        return "".join(s)
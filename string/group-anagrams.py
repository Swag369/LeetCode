class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrammap = dict()

        for string in strs:
            c = list(string)
            c.sort()
            c= "".join(c)

            if c not in anagrammap:
                anagrammap[c] = [string]
            else:
                anagrammap[c].append(string)

        # print(anagrammap)

        ret = []

        for k in anagrammap.keys():
            ret.append(anagrammap[k])
        return ret
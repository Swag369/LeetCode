class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        map2 = {}
        for c in s:
            map[c] = map.get(c, 0) + 1
        for c in t:
            map2[c] = map2.get(c, 0) + 1

        for key in map2:
            if map.get(key, 0) != map2.get(key, 0):
                return False
        for key in map:
            if map.get(key, 0) != map2.get(key, 0):
                return False
        return True
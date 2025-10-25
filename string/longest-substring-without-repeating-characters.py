class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        a = dict()
        start = 0
        cur = 0
        maxlen = 0

        for c in s:
            if c not in a or a[c] < start:
                a[c] = cur
                maxlen = max(maxlen, cur+1 - start)
            else:
                start = a[c] + 1
                # to_remove = []
                # for letter_seen in a.keys():
                #     if a[letter_seen] < start:
                #         to_remove.append(letter_seen)
                # for i in to_remove:
                #     del a[i]
                a[c] = cur
                maxlen = max(maxlen, cur+1 - start)
            # print(a, start, cur, maxlen)
            cur = cur + 1
        return maxlen
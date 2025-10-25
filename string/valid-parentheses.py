class Solution:
    def isValid(self, g: str) -> bool:
        s = []

        for c in g:
            print(c)
            if c == '[' or c == '{' or c == '(':
                s.append(c)
                # print(s)
            else:
                if(len(s) == 0):
                    return False
                if ord(c) == ord(s[-1]) + 1 or ord(c) == ord(s[-1]) + 2:
                    s.pop()
                else:
                    return False
        
        print(s)
        if len(s) == 0:
            return True
        return False
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        ans = []

        # print(path)
        # print(path.split("/"))
        a = path.split("/")
        for i in a:
            if i == "":
                continue
            if i == ".":
                continue
            if i == "..":
                if len(ans) > 0:
                    ans.pop(-1)
            else:
                ans.append(i)

        return "/" + "/".join(ans)
        # canonical_path = ['/']
        # i = 1

        # while i < len(path):
        #     if path[i] == '/':
                
        #         if canonical_path[-1] == "/":
        #             continue
        #         else:
        #             canonical_path.append("/")
                
        #     if path[i] == ".":


        #     i += 1

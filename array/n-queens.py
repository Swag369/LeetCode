class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        def place(matrix, column):
            matrix = [list(matrix[i]) for i in range(len(matrix))]
            # print("got", matrix, "with", column) #mark whole column down
            for i in range(len(matrix)):
                matrix[i][column] = 1
            # print("marked col")
            # print(matrix)
            side = column
            down = 0
            while side >= 0 and down < len(matrix):
                matrix[down][side] = 1
                side -= 1
                down += 1
            # print("marked diagonal down to left")
            # print(matrix)
            side = column
            down = 0
            while side < len(matrix[0]) and down < len(matrix):
                # print("side, down", side, down)
                matrix[down][side] = 1
                side += 1
                down += 1
            # print("marked diagonal down to right")
            # print(matrix)
            matrix[0][column] = 'Q'
            return matrix

        def helper(matrix):
        

            # print("called on last", len(matrix), matrix)

            if len(matrix) == 1: # if putting last queen
                ret = []
                for i in range(len(matrix[0])):
                    if matrix[0][i] == 0:
                        copy = list(matrix[0])
                        copy[i] = 'Q'
                        ret.append([copy])
                # print("lowest level returning", ret)
                return ret

            ret = []
            for column in range(n):
                if matrix[0][column] == 0:
                    placed_matrix = place(matrix, column)
                    # print(len(matrix), "passing on, using", column, "so passing", placed_matrix)
                    remaining_placed_matrix = placed_matrix[1:]
                    possible_children = helper(remaining_placed_matrix)
                    # print("for placement", placed_matrix[:1][0], "of", placed_matrix, "at len", len(matrix), "got kids", possible_children)
                    # possible_children_with_my_placement = []
                    for i in possible_children:
                        i.insert(0, placed_matrix[:1][0])
                    # print("helper returning", possible_children)

                    ret.extend(possible_children)

            # print("bottom", len(matrix), "gave", ret)
            # print("was given", matrix)
            return ret

        ret = helper([[0 for _ in range(n)] for _ in range(n)])
        # print(ret)
        for l in ret:
            # print("l is", l)
            for i in range(len(l)):
                for j in range(len(l[0])):
                    # print("LAST")
                    # print(l)
                    # print(l[i])
                    if l[i][j] != 'Q':
                        l[i][j] = '.'
        for l in ret:
            for i in range(len(l)):
                l[i] = "".join(l[i])
        return ret

        # place([[0,0,0],[0,0,0],[0,0,0]], 0)
        # print("NEW")
        # place([[0,0,0],[0,0,0],[0,0,0]], 1)
        # print("NEW")
        # place([[0,0],[0,0]], 0)        








        # def place(matrix, column):
        #     matrix = [list(matrix[i]) for i in range(len(matrix))]
        #     # print("got", matrix, "with", column) #mark whole column down
        #     for i in range(len(matrix)):
        #         matrix[i][column] = 1
        #     # print("marked col")
        #     # print(matrix)
        #     side = column
        #     down = 0
        #     while side >= 0 and down < len(matrix):
        #         matrix[down][side] = 1
        #         side -= 1
        #         down += 1
        #     # print("marked diagonal down to left")
        #     # print(matrix)
        #     side = column
        #     down = 0
        #     while side < len(matrix[0]) and down < len(matrix):
        #         # print("side, down", side, down)
        #         matrix[down][side] = 1
        #         side += 1
        #         down += 1
        #     # print("marked diagonal down to right")
        #     # print(matrix)
        #     return matrix

        # def helper(matrix):

        #     print("called on last", len(matrix))

        #     if len(matrix) == 1: # if putting last queen
        #         print("bottom row", len(matrix), "gave", n - sum(matrix[0]))
        #         return n - sum(matrix[0])

        #     solutions = 0
        #     for column in range(n):
        #         if matrix[0][column] == 0:
        #             placed_matrix = place(matrix, column)
        #             print(len(matrix), "passing on, using", column, "so passing", placed_matrix)
        #             remaining_placed_matrix = placed_matrix[1:]
        #             solutions += helper(remaining_placed_matrix)

        #     print("bottom", len(matrix), "gave", solutions)
        #     print("was given", matrix)
        #     return solutions

        # return helper([[0 for _ in range(n)] for _ in range(n)])

        # # place([[0,0,0],[0,0,0],[0,0,0]], 0)
        # # print("NEW")
        # # place([[0,0,0],[0,0,0],[0,0,0]], 1)
        # # print("NEW")
        # # place([[0,0],[0,0]], 0)
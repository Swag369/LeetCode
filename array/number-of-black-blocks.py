class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        
        counts = [0,0,0,0,0]
        black_squares = set(list(map(lambda a: (a[0],a[1]), coordinates)))

        visited_blocks = set()

        # print(counts)
        # print(black_squares)
        # print(coordinates)

        counts[0] = (m-1)*(n-1)

        for i in coordinates:
            x = i[0]
            y = i[1]


            a = 0
            if (x,y) not in visited_blocks and x >= 0 and y >= 0 and x <m-1 and y < n-1:
                a += 1 if (x,y) in black_squares else 0
                a += 1 if (x+1,y) in black_squares else 0
                a += 1 if (x,y+1) in black_squares else 0
                a += 1 if (x+1,y+1) in black_squares else 0
                # print("looking at", x, y, "in visited blocks?", (x,y) in visited_blocks, "summed", a)
                # print(counts)

            visited_blocks.add((x,y))
            counts[a] += 1
            counts[0] -= 1

            x -= 1
            y-= 1
            a = 0
            if (x,y) not in visited_blocks and x>=0 and y>=0 and x <m-1 and y < n-1:
                a += 1 if (x,y) in black_squares else 0
                a += 1 if (x+1,y) in black_squares else 0
                a += 1 if (x,y+1) in black_squares else 0
                a += 1 if (x+1,y+1) in black_squares else 0
                # print("looking at", x, y, "in visited blocks?", (x,y) in visited_blocks, "summed", a)
            visited_blocks.add((x,y))
            counts[a] += 1
            counts[0] -= 1

            x += 1
            a = 0
            if (x,y) not in visited_blocks and x>=0 and y>=0 and x <m-1 and y < n-1:
                a += 1 if (x,y) in black_squares else 0
                a += 1 if (x+1,y) in black_squares else 0
                a += 1 if (x,y+1) in black_squares else 0
                a += 1 if (x+1,y+1) in black_squares else 0
                # print("looking at", x, y, "in visited blocks?", (x,y) in visited_blocks, "summed", a)
            visited_blocks.add((x,y))
            counts[a] += 1
            counts[0] -= 1

            x -= 1
            y += 1
            a = 0
            if (x,y) not in visited_blocks and x>=0 and y>=0 and x <m-1 and y < n-1:
                a = 0
                a += 1 if (x,y) in black_squares else 0
                a += 1 if (x+1,y) in black_squares else 0
                a += 1 if (x,y+1) in black_squares else 0
                a += 1 if (x+1,y+1) in black_squares else 0
                # print("looking at", x, y, "in visited blocks?", (x,y) in visited_blocks, "summed", a)
            visited_blocks.add((x,y))
            counts[a] += 1
            counts[0] -= 1




        return counts
        # coords = dict()

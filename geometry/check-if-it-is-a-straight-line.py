class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if coordinates[1][0] == coordinates[0][0] and coordinates[2][0] != coordinates[1][0]:
            return False

        if coordinates[1][0] == coordinates[0][0]:
            x= coordinates[0][0]
            for i in coordinates:
                if i[0] != x:
                    return False
            return True

        slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])

        for i in range(len(coordinates)-1):

            if (coordinates[i+1][0] - coordinates[i+0][0]) == 0:
                return False

            a = (coordinates[i+1][1] - coordinates[i+0][1])/(coordinates[i+1][0] - coordinates[i+0][0])

            if slope != a:
                return False

        return True
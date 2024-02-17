class Solution:
    def isPathCrossing(self, path: str) -> bool:
        position, visited_positions = [0, 0], set()
        directions = {"N": [1, 0], "E": [0, 1], "S": [-1, 0], "W": [0, -1]}

        for character in path:
            visited_positions.add(tuple(position))
            position[0] += directions[character][0]
            position[1] += directions[character][1]

            if tuple(position) in visited_positions:
                return True

        return False

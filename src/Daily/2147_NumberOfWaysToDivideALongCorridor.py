class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats_count = corridor.count("S")
        if seats_count <= 1 or seats_count % 2 == 1:
            return 0
        modulo = int(1e9) + 7
        actual_seat_count = 0
        actual_plant_count = 0
        result = 1
        for item in corridor:
            if item == "S":
                actual_seat_count += 1
            if item == "P" and actual_seat_count == 2:
                actual_plant_count += 1
            if item == "S" and actual_seat_count == 4:
                result *= actual_plant_count + 1
                result = result % modulo
                actual_plant_count = 0
                actual_seat_count = 2

        return result

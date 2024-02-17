class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleets_count = 0
        cars = sorted(zip(position, speed))
        previous_car = cars[len(cars) - 1]

        for index in range(len(cars) - 2, -1, -1):
            car_position, car_speed = cars[index]
            previous_turns = (target - previous_car[0]) / previous_car[1]
            current_turns = (target - car_position) / car_speed
            if previous_turns < current_turns:
                fleets_count += 1
                previous_car = car_position, car_speed

        return fleets_count + 1

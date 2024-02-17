from sortedcontainers import SortedList


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        previous_temperatures: list[int] = []
        next_days = [0 for _ in range(len(temperatures))]

        for index in range(len(temperatures) - 1, -1, -1):
            temperature = temperatures[index]

            while previous_temperatures and temperature >= temperatures[previous_temperatures[-1]]:
                previous_temperatures.pop()

            if previous_temperatures:
                next_days[index] = previous_temperatures[-1] - index

            previous_temperatures.append(index)

        return next_days

    def nlogn_dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        previous_temperatures = SortedList()
        next_days = [0 for _ in range(len(temperatures))]

        for index, temperature in enumerate(temperatures):
            while previous_temperatures:
                if previous_temperatures[0][0] < temperature:
                    next_days[previous_temperatures[0][1]] = index - previous_temperatures[0][1]
                    previous_temperatures.pop(0)
                else:
                    break
            previous_temperatures.add((temperature, index))

        return next_days

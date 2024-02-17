class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        cities = set()
        for _, city_end in paths:
            cities.add(city_end)

        for city_start, _ in paths:
            if city_start in cities:
                cities.remove(city_start)

        return list(cities)[0]

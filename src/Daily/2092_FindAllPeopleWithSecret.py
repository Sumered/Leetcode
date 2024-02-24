import heapq


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        visited = [False for _ in range(n)]
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for first_person, second_person, time in meetings:
            graph[first_person].append((time, second_person))
            graph[second_person].append((time, first_person))

        meeting_order = []
        meeting_order.append((0, 0))
        meeting_order.append((0, firstPerson))

        while meeting_order:
            time, person = heapq.heappop(meeting_order)

            if visited[person]:
                continue

            visited[person] = True

            for meeting_time, met_person in graph[person]:
                if time <= meeting_time:
                    heapq.heappush(meeting_order, (meeting_time, met_person))

        result = []

        for index in range(n):
            if visited[index]:
                result.append(index)

        return result

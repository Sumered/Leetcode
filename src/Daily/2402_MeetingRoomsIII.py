class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        rooms = [-1 for _ in range(n)]
        rooms_meetings = [0 for _ in range(n)]
        for meeting in meetings:
            room_chosen = self.__get_first_available_room(rooms, meeting[0])

            if rooms[room_chosen] <= meeting[0]:
                rooms[room_chosen] = meeting[1]
            else:
                rooms[room_chosen] = meeting[1] + (rooms[room_chosen] - meeting[0])

            rooms_meetings[room_chosen] += 1

        return rooms_meetings.index(max(rooms_meetings))

    def __get_first_available_room(self, rooms: list[int], start: int) -> int:
        first_available_time, first_available_index = int(1e9), -1
        for index, room in enumerate(rooms):
            if room <= start:
                return index
            if room < first_available_time:
                first_available_time = room
                first_available_index = index

        return first_available_index

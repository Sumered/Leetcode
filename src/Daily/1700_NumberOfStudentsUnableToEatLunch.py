from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_new = deque()
        students_old = deque(students)
        sandwiches = list(reversed(sandwiches))

        while sandwiches:
            match_found = False
            while students_old:
                if students_old[0] == sandwiches[-1]:
                    match_found = True
                    sandwiches.pop()
                    students_old.popleft()
                else:
                    student = students_old.popleft()
                    students_new.append(student)

            if not match_found:
                return len(students_new)

            students_old = students_new
            students_new = deque()

        return 0

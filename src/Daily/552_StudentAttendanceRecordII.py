from dataclasses import dataclass, field


class Solution:
    MODULO = int(1e9) + 7

    @dataclass
    class State:
        @dataclass
        class LateCount:
            late_zero: int = 0
            late_once: int = 0
            late_twice: int = 0

            @property
            def sum(self) -> int:
                return self.late_zero + self.late_once + self.late_twice

            def modulo(self) -> None:
                self.late_zero = self.late_zero % Solution.MODULO
                self.late_once = self.late_once % Solution.MODULO
                self.late_twice = self.late_twice % Solution.MODULO

        absent_zero: LateCount = field(default_factory=LateCount)
        absent_once: LateCount = field(default_factory=LateCount)

    def checkRecord(self, n: int) -> int:
        current_state = Solution.State(absent_zero=Solution.State.LateCount(1, 1, 0), absent_once=Solution.State.LateCount(1, 0, 0))
        next_state = Solution.State()

        for _ in range(1, n):
            next_state = Solution.State()
            # Absent zero
            next_state.absent_zero.late_zero = (
                current_state.absent_zero.late_zero + current_state.absent_zero.late_once + current_state.absent_zero.late_twice
            )  # add P to them

            next_state.absent_zero.late_once = current_state.absent_zero.late_zero  # add L to it
            next_state.absent_zero.late_twice = current_state.absent_zero.late_once  # add L to it

            # Absent once
            next_state.absent_once.late_zero = (
                current_state.absent_once.late_zero + current_state.absent_once.late_once + current_state.absent_once.late_twice
            )  # add P to them

            next_state.absent_once.late_once = current_state.absent_once.late_zero  # add L to it
            next_state.absent_once.late_twice = current_state.absent_once.late_once  # add L to it

            # Transform from Absent zero to once
            next_state.absent_once.late_zero += (
                current_state.absent_zero.late_zero + current_state.absent_zero.late_once + current_state.absent_zero.late_twice
            )

            current_state = next_state
            current_state.absent_zero.modulo()
            current_state.absent_once.modulo()

        return (current_state.absent_zero.sum + current_state.absent_once.sum) % Solution.MODULO

__all__ = ["Testable"]

from src.day8 import Solution
from tests.helper import Testable

TEST_CASE = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "0", ".", ".", "."],
    [".", ".", ".", ".", ".", "0", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "0", ".", ".", ".", "."],
    [".", ".", ".", ".", "0", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "A", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "A", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "A", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]


class TestSolution(Testable):
    def test_find_closest_antinodes(self) -> None:
        solution = Solution(TEST_CASE)

        antinodes = solution.count_closest_antinodes()

        assert antinodes == 14

    def test_find_all_antinodes(self) -> None:
        solution = Solution(TEST_CASE)

        antinodes = solution.count_all_antinodes()

        assert antinodes == 34
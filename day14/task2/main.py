"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=14 ; task=2)
https://adventofcode.com/2024/day/14
Answer: 6876 (in task2.out lines 735627 - 735730)
"""

import copy
import re
import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from day14.task1.main import Robot
from utils import measure, print_matrix


@measure
def main():
    MATRIX_SIZE = (101, 103)  # 11, 7 for test input
    EMPTY_MATRIX = [['.'] * MATRIX_SIZE[0] for _ in range(MATRIX_SIZE[1])]
    robots = []
    for line in sys.stdin:
        x, y, vel_x, vel_y = list(map(int, re.findall(r'-?\d+', line)))
        robot = Robot((x, y), (vel_x, vel_y))
        robots.append(robot)

    for i in range(10000):
        matrix = copy.deepcopy(EMPTY_MATRIX)
        for robot in robots:
            robot.computeNextPos(MATRIX_SIZE)
        for robot in robots:
            matrix[robot.pos[1]][robot.pos[0]] = 'X'
        print(i)
        print_matrix(matrix, file=sys.stdout)
        print()


if __name__ == "__main__":
    main()

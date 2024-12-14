"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=14 ; task=1)
https://adventofcode.com/2024/day/14
"""

import re
import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import measure


class Robot():
    def __init__(self, pos: tuple[int, int], vel: tuple[int, int]):
        self.pos = pos
        self.vel = vel

    def computeNextPos(self, matrix_size: tuple[int, int]):
        new_x = (self.pos[0] + self.vel[0]) % matrix_size[0]
        new_y = (self.pos[1] + self.vel[1]) % matrix_size[1]
        self.pos = (new_x, new_y)

    def computeNextPosAfterN(self, matrix_size: tuple[int, int], steps: int):
        new_x = (self.pos[0] + self.vel[0] * steps) % matrix_size[0]
        new_y = (self.pos[1] + self.vel[1] * steps) % matrix_size[1]
        self.pos = (new_x, new_y)

    def __repr__(self):
        return '(' + str(self.pos) + ', ' + str(self.vel) + ')'


@measure
def main():
    MATRIX_SIZE = (101, 103)  # 11, 7 for test input
    robots = []
    for line in sys.stdin:
        x, y, vel_x, vel_y = list(map(int, re.findall(r'-?\d+', line)))
        robot = Robot((x, y), (vel_x, vel_y))
        robot.computeNextPosAfterN(MATRIX_SIZE, 100)
        robots.append(robot)

    x = MATRIX_SIZE[0] // 2
    y = MATRIX_SIZE[1] // 2
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if robot.pos[0] < x:
            if robot.pos[1] < y:
                quadrants[0] += 1
            elif robot.pos[1] > y:
                quadrants[2] += 1
        elif robot.pos[0] > x:
            if robot.pos[1] < y:
                quadrants[1] += 1
            elif robot.pos[1] > y:
                quadrants[3] += 1

    res = quadrants[0]
    for elem in quadrants[1:]:
        res *= elem

    print(res)


if __name__ == "__main__":
    main()

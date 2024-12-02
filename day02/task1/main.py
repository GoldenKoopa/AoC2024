"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=2 ; task=1)
https://adventofcode.com/2024/day/2
"""

import functools
import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())

print = functools.partial(print, flush=True)


def is_monotone(lst):
    if len(lst) < 2:
        return True

    if lst[0] < lst[1]:
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        return True

    if lst[0] > lst[1]:
        for i in range(len(lst) - 1):
            if lst[i] <= lst[i + 1]:
                return False
        return True


def has_valid_distances(lst):
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def main():
    sum = 0
    for line in sys.stdin:
        report = list(map(int, line.split()))
        if is_monotone(report) and has_valid_distances(report):
            sum += 1

    print(sum)


if __name__ == "__main__":
    main()

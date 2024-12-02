"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=1 ; task=1)
"""

import functools
import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())

print = functools.partial(print, flush=True)


def main():
    left_list = []
    right_list = []
    for line in sys.stdin:
        line_values = line.split("   ")
        left_list.append(int(line_values[0]))
        right_list.append(int(line_values[1]))

    left_list.sort()
    right_list.sort()

    sum = 0
    for i in range(len(left_list)):
        sum += abs(right_list[i] - left_list[i])

    print(sum)


if __name__ == "__main__":
    main()

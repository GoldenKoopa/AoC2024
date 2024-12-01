"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=1 ; task=2)
"""

import sys
import pathlib
sys.path.append(pathlib.Path(__file__).parent.parent.parent.absolute().as_posix())

import functools
print = functools.partial(print, flush=True)


def main():
    left_list = []
    right_list = []
    for line in sys.stdin:
        line_values = line.split("   ")
        left_list.append(int(line_values[0]))
        right_list.append(int(line_values[1]))



    sum = 0
    for elem in left_list:
        sum += right_list.count(elem) * elem

    print(sum)




if __name__ == "__main__":
    main()

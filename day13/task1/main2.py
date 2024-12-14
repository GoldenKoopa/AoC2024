"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=13 ; task=1)
https://adventofcode.com/2024/day/13
"""

import sys
import pathlib
import re
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import measure


@measure
def main():
    machines = sys.stdin.read()
    machines = machines.split('\n\n')
    tokens = 0
    for machine in machines:
        swapped = False
        a, b, prize = machine.splitlines()
        a = tuple(map(int, re.findall(r'\d+', a)))
        b = tuple(map(int, re.findall(r'\d+', b)))
        prize = tuple(map(int, re.findall(r'\d+', prize)))
        if 3 * b[0] > a[0]:
            a, b = b, a
            swapped = True
        i = 0
        while (tmp := prize[0] - i * a[0]) > 0:
            if tmp % b[0] == 0:
                times_pressed_b = tmp // b[0]
                if i*a[1] + times_pressed_b*b[1] == prize[1]:
                    if swapped:
                        tokens += i + 3 * times_pressed_b
                    else:
                        tokens += times_pressed_b + 3 * i
                    break

            i += 1

    print(tokens)


if __name__ == "__main__":
    main()

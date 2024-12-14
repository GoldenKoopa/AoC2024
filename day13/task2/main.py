"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=13 ; task=2)
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
        ints = re.findall(r'\d+', machine)
        a, b, d, e, c, f = list(map(int, ints))
        c += 10000000000000
        f += 10000000000000
        x = (a * f - b * c) / (d * b - e * a)
        y = (c + x * d) / a
        if x % 1 == 0 and y % 1 == 0:
            tokens += abs(x) + abs(y) * 3

    print(int(tokens))


if __name__ == "__main__":
    main()

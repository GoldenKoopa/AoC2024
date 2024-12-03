"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=3 ; task=1)
https://adventofcode.com/2024/day/3
"""

import functools
import sys
import pathlib
import re
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())

print = functools.partial(print, flush=True)


def main():
    total = 0
    for line in sys.stdin:
        occurences = re.findall(r'mul\((\d{3}|\d{2}|\d{1}),(\d{3}|\d{2}|\d{1})\)', line)
        for occ in occurences:
            total += int(occ[0]) * int(occ[1])
    
    print(total)


if __name__ == "__main__":
    main()

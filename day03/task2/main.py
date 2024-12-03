"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=3 ; task=2)
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
    is_enabled = True
    
    for line in sys.stdin:
        conditions = re.finditer(r'(do\(\))|(don\'t\(\))', line)
        occurences = re.finditer(r'mul\((\d{3}|\d{2}|\d{1}),(\d{3}|\d{2}|\d{1})\)', line)
        all = [occ for occ in occurences] + [condition for condition in conditions]
        all.sort(key=lambda elem: elem.start())
        for elem in all:
            elem = elem.group(0)
            if elem == 'do()':
                is_enabled = True
            elif elem == 'don\'t()':
                is_enabled = False
            elif not is_enabled:
                continue
            else:
                factors = re.findall(r'\d{1,}', elem)
                total += int(factors[0]) * int(factors[1])
    
    print(total)

if __name__ == "__main__":
    main()

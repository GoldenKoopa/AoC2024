"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=7 ; task=1)
https://adventofcode.com/2024/day/7
"""

import functools
import sys
import pathlib
from icecream import ic
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())

print = functools.partial(print, flush=True)


def main():
    total = 0
    for line in sys.stdin:
        line_total, nums = line.split(":")
        line_total = int(line_total)
        nums = list(map(int, nums.split()))
        
        results = []
        while nums:
            current_num = nums.pop(0)
            if len(results) == 0:
                results.append(current_num)
                continue
            tmp = []
            for result in results:
                tmp.append(result * current_num)
                tmp.append(result + current_num)
            results = tmp

        if line_total in results:
            total += line_total
    
    print(total)
        
        


if __name__ == "__main__":
    main()

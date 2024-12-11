"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=11 ; task=1)
https://adventofcode.com/2024/day/11
"""

import sys
import pathlib
from icecream import ic
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import measure
import numpy as np



@measure
def main():
    stones = list(map(int, sys.stdin.read().strip().split()))

    for _ in range(25):
        temp = []
        for stone in stones:
            if stone == 0:
                temp.append(1)
            elif (digits := len(str(stone))) % 2 == 0:
                temp.append(int(str(stone)[:digits//2]))
                temp.append(int(str(stone)[digits//2:]))
            else:
                temp.append(stone * 2024)
        stones = temp
    
    print(len(stones))
    



if __name__ == "__main__":
    main()

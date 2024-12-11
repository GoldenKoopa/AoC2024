"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=11 ; task=2)
https://adventofcode.com/2024/day/11
"""

import sys
import pathlib
from icecream import ic
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import measure


class myInt(int):
    def __new__(cls, value, count=1):
        instance = super().__new__(cls, value)
        instance.count = count
        return instance
        


@measure
def main():
    stones = list(map(myInt, sys.stdin.read().strip().split()))
    stones_dict = {}
    stones_transform_dict = {}
    
    stones_dict[0] = 0
    stones_dict[1] = 1
    stones_transform_dict[0] = [1]
    
    i = 2
    for stone in stones:
        if stone in stones_dict.values():
            continue
        stones_dict[i] = stone
        stones[stones.index(stone)] = myInt(i)
        i += 1
    
        

    for _ in range(75):
        temp = []
        for stone in stones:
            if stone == 0:
                if 1 in temp:
                    temp[temp.index(1)].count += stone.count
                else:
                    temp.extend([myInt(1, stone.count)])
                continue
            if stones_transform_dict.get(stone, None) is not None:
                for elem in stones_transform_dict.get(stone):
                    if elem in temp:
                        temp[temp.index(elem)].count += stone.count
                    else:
                        temp.extend([myInt(elem, stone.count)])
                continue
            
            stone_int = stones_dict[stone]
            if (digits := len(str(stone_int))) % 2 == 0:
                num1 = int(str(stone_int)[:digits//2])
                num2 = int(str(stone_int)[digits//2:])
                try:
                    num1_address = list(stones_dict.values()).index(num1)
                except ValueError as e:
                    stones_dict[i] = num1
                    num1_address = i
                    i += 1
                try:
                    num2_address = list(stones_dict.values()).index(num2)
                except ValueError as e:
                    stones_dict[i] = num2
                    num2_address = i
                    i += 1
                for elem in [num1_address, num2_address]:
                    if elem in temp:
                        temp[temp.index(elem)].count += stone.count
                    else:
                        temp.extend([myInt(elem, stone.count)])
                stones_transform_dict[stone] = [num1_address, num2_address]    
            else:
                num = stone_int * 2024
                try:
                    num_address = list(stones_dict.values()).index(num)
                except ValueError as e:
                    stones_dict[i] = num
                    num_address = i
                    i += 1
                stones_transform_dict[stone] = [num_address]
                if num_address in temp:
                    temp[temp.index(num_address)].count += stone.count
                else:
                    temp.extend([myInt(num_address, stone.count)])
            
            
            
            
        stones = temp

    print(sum([stone.count for stone in stones]))


if __name__ == "__main__":
    main()

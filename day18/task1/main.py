"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=18 ; task=1)
https://adventofcode.com/2024/day/18
"""

import sys
import pathlib
from icecream import ic
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import measure


DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def search(rows: int, columns: int, start: tuple[int, int], end: tuple[int, int], obstacles:list[tuple[int, int]]):
    cost = {}
    cost = {(r, c): float('inf') for r in range(rows) for c in range(columns)}

            
    cost[start] = 0
    queue = [start]
    
    while queue:
        tile = queue.pop()
        for dir in DIRS:
            r, c = tile[0] + dir[0], tile[1] + dir[1]
            if (r, c) not in cost.keys() or (r, c) in obstacles:
                continue
            if cost[tile] + 1 < cost[(r, c)]:
                cost[(r, c)] = cost[tile] + 1
                queue.append((r, c))
    
    return cost[end]


        

@measure
def main():
    n = 1024
    bytes = []
    for line in sys.stdin:
        bytes.append(tuple(map(int, line.split(','))))
    
    bytes = bytes[:n]
    
    result = search(71, 71, (0, 0), (70, 70), bytes)
    print(result)



if __name__ == "__main__":
    main()

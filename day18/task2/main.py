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
import heapq


DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def search(rows: int, columns: int, start: tuple[int, int], end: tuple[int, int], obstacles: list[tuple[int, int]]):
    obstacles_set = set(obstacles)
    cost = {(r, c): float('inf') for r in range(rows) for c in range(columns)}
    cost[start] = 0
    queue = [(0, start)]
    
    def get_neighbors(tile):
        r, c = tile
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in obstacles_set:
                yield (nr, nc)
    
    while queue:
        current_cost, tile = heapq.heappop(queue)
        
        if tile == end:
            return current_cost
        
        if current_cost > cost[tile]:
            continue
        
        for neighbor in get_neighbors(tile):
            new_cost = current_cost + 1
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
    
    return float('inf')

        

@measure
def main():
    n = 1024
    bytes = []
    for line in sys.stdin:
        bytes.append(tuple(map(int, line.split(','))))
    
    for i in range(n, len(bytes)):
        new_bytes = bytes[:i]
        result = search(71, 71, (0, 0), (70, 70), new_bytes)
        if result == float('inf'):
            print(new_bytes[-1])
            break
        if i % 20 == 0:
            ic(result)
            ic(i)



if __name__ == "__main__":
    main()

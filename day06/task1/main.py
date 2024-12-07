"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=6 ; task=1)
https://adventofcode.com/2024/day/6
"""

import functools
import sys
import pathlib
from icecream import ic
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import pad_matrix, search_matrix, print_matrix

print = functools.partial(print, flush=True)


def main():
    guard_map = sys.stdin.read().splitlines()
    guard_map = [list(line) for line in guard_map]
    guard_map = pad_matrix(guard_map, 'O', 1)
    guard_pos = search_matrix(guard_map, '^')[0]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction = directions[0]
    
    while True:
        next_tile = guard_map[guard_pos[0] + current_direction[0]][guard_pos[1] + current_direction[1]]
        if next_tile == '#':
            current_direction = directions[(directions.index(current_direction) + 1) % 4]
            continue
        guard_map[guard_pos[0]][guard_pos[1]] = 'X'
        if next_tile == 'O':
            break
        guard_pos = tuple(map(sum, zip(guard_pos, current_direction)))

    # ic(print_matrix(guard_map))
    print(sum([sum([1 if char == 'X' else 0 for char in line]) for line in guard_map]))


if __name__ == "__main__":
    main()

"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=6 ; task=2)
https://adventofcode.com/2024/day/6
"""

import functools
import sys
import pathlib
from icecream import ic
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import search_matrix, pad_matrix, print_matrix
import copy

print = functools.partial(print, flush=True)


def main():
    guard_map = sys.stdin.read().splitlines()
    guard_map = [[[value, None] for value in list(line)] for line in guard_map]
    
    guard_map = pad_matrix(guard_map, ['O', None], 1)
    initial_guard_pos = search_matrix(guard_map, ['^', None])[0]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    initial_current_direction = directions[0]
    
    total = 0
    for r in range(len(guard_map)):
        for c in range(len(guard_map[0])):
            if guard_map[r][c] == ['O', None] or guard_map[r][c] == ['#', None]:
                continue
            ic(r, c)
            guard_map_copy = copy.deepcopy(guard_map)
            guard_map_copy[r][c] = ['#', None]
            guard_pos = initial_guard_pos
            current_direction = initial_current_direction
            # if r == 6 and c == 6:
            #     print_matrix([[pair[0] for pair in row] for row in guard_map_copy])
            #     exit()
            if search_map(guard_map_copy, guard_pos, directions, current_direction):
                total += 1
            

    print(total)

def search_map(guard_map, guard_pos, directions, current_direction):
    reversed = False
    last_three_turns = [False, False, False]
    while True:
        if not last_three_turns[0] and last_three_turns[1] and not last_three_turns[2]:
            reversed = False
        elif last_three_turns[0] and last_three_turns[1]:
            if reversed:
                return True
            reversed = True
        next_tile = guard_map[guard_pos[0] + current_direction[0]][guard_pos[1] + current_direction[1]]
        if next_tile[0] == '#':
            current_direction = directions[(directions.index(current_direction) + 1) % 4]
            last_three_turns = [True, last_three_turns[0], last_three_turns[1]]
            continue
        else:
            last_three_turns = [False, last_three_turns[0], last_three_turns[1]]
        guard_map[guard_pos[0]][guard_pos[1]][0] = 'X'
        guard_map[guard_pos[0]][guard_pos[1]][1] = directions.index(current_direction)
        if next_tile[0] == 'X' and next_tile[1] == directions.index(current_direction):
            return True
        if next_tile[0] == 'O':
            return False
        guard_pos = tuple(map(sum, zip(guard_pos, current_direction)))


if __name__ == "__main__":
    main()

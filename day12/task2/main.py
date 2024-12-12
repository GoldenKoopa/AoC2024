"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=12 ; task=2)
https://adventofcode.com/2024/day/12
"""

import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import pad_matrix, search_matrix, flood_fill, measure


def get_unique_edges(matrix, r, c, pattern, tiles):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited_tiles = set()
    total_edges = 0
    for r2, c2, in tiles:
        for dir in directions:
            r3 = r2 + dir[0]
            c3 = c2 + dir[1]
            if matrix[r3][c3] != pattern:
                dir2 = directions[(directions.index(dir) + 1) % 4]
                dir3 = directions[(directions.index(dir) - 1) % 4]
                if (r2 + dir2[0], c2 + dir2[1], dir) not in visited_tiles \
                and (r2 + dir3[0], c2 + dir3[1], dir) not in visited_tiles:
                    total_edges += 1
                visited_tiles.add((r2, c2, dir))

    return total_edges


@measure
def main():
    garden = [list(line.strip()) for line in sys.stdin.readlines()]
    garden = pad_matrix(garden, 0, 1)
    total = 0
    for r in range(1, len(garden) - 1):
        for c in range(1, len(garden[0]) - 1):
            if garden[r][c] == 0:
                continue
            flood_fill(garden, r, c, 1, garden[r][c])
            tiles = search_matrix(garden, 1)
            area = len(tiles)
            edges = get_unique_edges(garden, r, c, 1, tiles)
            total += edges * area
            flood_fill(garden, r, c, 0, 1)

    print(total)


if __name__ == "__main__":
    main()

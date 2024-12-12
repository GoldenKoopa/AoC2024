"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=12 ; task=1)
https://adventofcode.com/2024/day/12
"""

from utils import pad_matrix, search_matrix, flood_fill, measure
import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())


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
            perimeter = 0
            for r2, c2 in tiles:
                if garden[r2+1][c2] != 1:
                    perimeter += 1
                if garden[r2-1][c2] != 1:
                    perimeter += 1
                if garden[r2][c2+1] != 1:
                    perimeter += 1
                if garden[r2][c2-1] != 1:
                    perimeter += 1
            total += perimeter * area
            flood_fill(garden, r, c, 0, 1)

    print(total)


if __name__ == "__main__":
    main()

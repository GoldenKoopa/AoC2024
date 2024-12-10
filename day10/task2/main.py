"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=10 ; task=2)
https://adventofcode.com/2024/day/10
"""

import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())
from utils import measure, pad_matrix, search_matrix


@measure
def main():
    topo_map = [list(map(int, list(line.strip())))
                for line in sys.stdin.readlines()]
    topo_map = pad_matrix(topo_map, '.', 1)
    trailheads = search_matrix(topo_map, 0)

    total = 0
    for trailhead in trailheads:
        current_tiles = [trailhead]
        for i in range(1, 10):
            temp = []
            for r, c in current_tiles:
                if topo_map[r + 1][c] == i:
                    temp.append((r + 1, c))
                if topo_map[r - 1][c] == i:
                    temp.append((r - 1, c))
                if topo_map[r][c + 1] == i:
                    temp.append((r, c + 1))
                if topo_map[r][c - 1] == i:
                    temp.append((r, c - 1))
            current_tiles = temp
        total += len(current_tiles)

    print(total)


if __name__ == "__main__":
    main()

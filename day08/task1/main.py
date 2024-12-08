"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=8 ; task=1)
https://adventofcode.com/2024/day/8
"""

import itertools
from utils import search_matrix
import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())


def main():
    antenna_map = sys.stdin.read().splitlines()
    antenna_map = [list(line) for line in antenna_map]
    unique_frequencies = {element for row in antenna_map for element in row}
    placement_set = set()
    for frequency in unique_frequencies:
        if frequency == '.':
            continue
        occurences = search_matrix(antenna_map, frequency)
        combinations = list(itertools.combinations(occurences, 2))
        for combination in combinations:
            combination2_inverse = tuple(
                list(map(lambda x: -x, combination[1])))
            diff = tuple(map(sum, zip(combination[0], combination2_inverse)))
            placement1 = tuple(map(sum, zip(combination[0], diff)))
            diff_inverse = tuple(list(map(lambda x: -x, diff)))
            placement2 = tuple(map(sum, zip(combination[1], diff_inverse)))

            for placement in [placement1, placement2]:
                if any(elem < 0 for elem in placement):
                    continue
                if placement[0] >= len(antenna_map) or placement[1] >= len(antenna_map[0]):
                    continue
                placement_set.add(placement)
    print(len(placement_set))


if __name__ == "__main__":
    main()

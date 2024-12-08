"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=8 ; task=2)
https://adventofcode.com/2024/day/8
"""

from math import gcd
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
            diff = reduce_fraction(*diff)
            diff_inverse = tuple(list(map(lambda x: -x, diff)))

            i = 0
            while True:
                placement = combination[0][0] + i * \
                    diff[0], combination[0][1] + i * diff[1]
                if any(elem < 0 for elem in placement):
                    break
                if placement[0] >= len(antenna_map) or placement[1] >= len(antenna_map[0]):
                    break
                placement_set.add(placement)
                i += 1
            i = 0
            while True:
                placement = combination[1][0] + i * \
                    diff_inverse[0], combination[1][1] + i * diff_inverse[1]
                if any(elem < 0 for elem in placement):
                    break
                if placement[0] >= len(antenna_map) or placement[1] >= len(antenna_map[0]):
                    break
                placement_set.add(placement)
                i += 1

    print(len(placement_set))


def reduce_fraction(a, b):
    d = gcd(a, b)
    a //= d
    b //= d
    return a, b


if __name__ == "__main__":
    main()

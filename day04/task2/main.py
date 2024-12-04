"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=4 ; task=2)
https://adventofcode.com/2024/day/4
"""

import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())

from utils import pad_matrix


def main():
    crossword = []
    for line in sys.stdin:
        crossword.append([elem for elem in line if elem != '\n'])
    crossword = pad_matrix(crossword, "X", 1)
    
    total = 0
    for r in range(len(crossword)):
        for c in range(len(crossword[0])):
            if crossword[r][c] == 'A':
                bool1 = crossword[r-1][c-1] == 'M' and crossword[r+1][c+1] == 'S'
                bool2 = crossword[r-1][c-1] == 'S' and crossword[r+1][c+1] == 'M'
                bool3 = crossword[r+1][c-1] == 'S' and crossword[r-1][c+1] == 'M'
                bool4 = crossword[r+1][c-1] == 'M' and crossword[r-1][c+1] == 'S'
                if (bool1 or bool2) and (bool3 or bool4):
                    total += 1
    
    print(total)
                    


if __name__ == "__main__":
    main()

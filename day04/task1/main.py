"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=4 ; task=1)
https://adventofcode.com/2024/day/4
"""

import sys
import pathlib
import re
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())



def main():
    crossword = []
    for line in sys.stdin:
        crossword.append([elem for elem in line if elem != '\n'])
        # crossword.append([elem for elem in line.split()])
    crossword_rotate = rotate_matrix(crossword)
    crossword_diagonal_1 = get_diagonal(crossword)
    crossword_diagonal_2 = get_diagonal(crossword_rotate)
    crossword_all = crossword + crossword_rotate + crossword_diagonal_1 + crossword_diagonal_2
    total = 0
    for line in crossword_all:
        line = "".join(line)
        occurences = re.finditer(r'(?=(XMAS|SAMX))', line)
        total += sum(1 for elem in occurences)
        
    print(total)    
    
def get_diagonal(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        lst = []
        for j in range(min(len(matrix[0]), i + 1)):
            lst.append(matrix[i-j][j])
        new_matrix.append(lst)
    for i in range(1, len(matrix[0])):
        lst = []
        for j in range(len(matrix[0]) - i):
            # lst.append([len(matrix) - i - j][len(matrix[0]) - j - 1])
            lst.append(matrix[len(matrix) - 1 - j][j + i])
        new_matrix.append(lst)
        
    return new_matrix
        
def rotate_matrix(matrix):
    return list(zip(*matrix[::-1]))
        


if __name__ == "__main__":
    main()

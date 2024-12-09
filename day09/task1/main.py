"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=9 ; task=1)
https://adventofcode.com/2024/day/9
"""

import sys



def main():
    diskmap = list(map(int, list(sys.stdin.read().strip())))
    disk_space = []
    for i, space in enumerate(diskmap):
        if i % 2 == 0:
            disk_space.extend([i // 2] * space)
        else:
            disk_space.extend(['.'] * space)
    
    while disk_space.index('.') < len(disk_space) - disk_space.count('.') - 1:
        for i in range(len(disk_space)):
            if disk_space[len(disk_space) - i - 1] != '.':
                disk_space[len(disk_space) - i - 1], disk_space[disk_space.index('.')] = \
                disk_space[disk_space.index('.')], disk_space[len(disk_space) - i - 1]
    
    total = 0
    for i, elem in enumerate(disk_space):
        if elem == '.':
            break
        total += elem * i
    
    print(total)


if __name__ == "__main__":
    main()

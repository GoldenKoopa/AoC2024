"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=9 ; task=2)
https://adventofcode.com/2024/day/9
"""

import functools
import sys
import pathlib
sys.path.append(pathlib.Path(
    __file__).parent.parent.parent.absolute().as_posix())

print = functools.partial(print, flush=True)


def main():
    diskmap = list(map(int, list(sys.stdin.read().strip())))
    disk_space = []
    for i, space in enumerate(diskmap):
        if i % 2 == 0:
            disk_space.append((i//2, space))
        else:
            disk_space.append(('.', space))
    
    
    largest_id = disk_space[-1][0]
    while True:
        file = next((file for file in disk_space if file[0] == largest_id), None)
        if file == '.':
            continue
        for j in range(disk_space.index(file)):
            if disk_space[j][0] != '.':
                continue
            if disk_space[j][1] >= file[1]:
                disk_space[disk_space.index(file)] = ('.', file[1])
                disk_space.insert(j, file)
                disk_space[j + 1] = (disk_space[j + 1][0], disk_space[j + 1][1] - disk_space[j][1])
                break
        largest_id -= 1
        if largest_id == -1:
            break
    
    disk_space_total = []
    [disk_space_total.extend([elem[0]] * elem[1]) for elem in disk_space]
    
    total = 0
    for i, elem in enumerate(disk_space_total):
        if elem == '.':
            continue
        total += int(elem) * i
    
    print(total)
    
    






if __name__ == "__main__":
    main()

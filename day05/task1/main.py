"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=5 ; task=1)
https://adventofcode.com/2024/day/5
"""

import sys


def main():
    page_order, updates = sys.stdin.read().split('\n\n')
    page_order = page_order.splitlines()
    updates = [list([value for value in line.split(',')])
               for line in updates.splitlines()]
    page_dict = {}
    for line in page_order:
        x, y = line.split('|')
        if (page_entry := page_dict.get(x)):
            page_entry.append(y)
        else:
            page_dict[x] = [y]

    ordered_updates = []
    for update in updates:
        ordered = True
        for i, page in enumerate(update):
            if (pages_after := page_dict.get(page)):
                for elem in pages_after:
                    if elem in update[:i]:
                        ordered = False
                        break
        if ordered:
            ordered_updates.append(update)

    ordered_updates = [list(map(int, update)) for update in ordered_updates]
    print(sum([update[(len(update) - 1)//2] for update in ordered_updates]))


if __name__ == "__main__":
    main()

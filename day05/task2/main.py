"""
Author: GoldenKoopa
Puzzle: Advent of Code (year=2024 ; day=5 ; task=2)
https://adventofcode.com/2024/day/5
"""

import functools
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

    def compare_pages(a, b):
        if a in page_dict.get(b, []):
            return 1
        if b in page_dict.get(a, []):
            return -1
        return 0

    unordered_updates = []
    for update in updates:
        ordered = True
        for i, page in enumerate(update):
            if (pages_after := page_dict.get(page)):
                for elem in pages_after:
                    if elem in update[:i]:
                        ordered = False
                        break
        if not ordered:
            unordered_updates.append(update)

    unordered_updates = [sorted(update, key=functools.cmp_to_key(
        compare_pages)) for update in unordered_updates]

    unordered_updates = [list(map(int, update))
                         for update in unordered_updates]
    print(sum([update[(len(update) - 1)//2] for update in unordered_updates]))


if __name__ == "__main__":
    main()

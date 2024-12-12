from typing import List, Tuple, Any


def is_valid(matrix: List[List[Any]], x: int, y: int, pattern: List[Any]) -> bool:
    """Check if the given coordinates are valid and match the pattern."""
    return (0 <= x < len(matrix[0]) and
            0 <= y < len(matrix) and
            matrix[y][x] in pattern)


def flood_fill(matrix: List[List[Any]], r: int, c: int, fill: any, pattern: List[Any]) -> None:
    """Perform flood fill on the matrix starting from (r, c)."""
    if not isinstance(pattern, list):
        pattern = [pattern]

    if not is_valid(matrix, c, r, pattern):
        return

    queue = [(c, r)]
    matrix[r][c] = fill

    while queue:
        current_x, current_y = queue.pop(0)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = current_x + dx, current_y + dy
            if is_valid(matrix, next_x, next_y, pattern):
                matrix[next_y][next_x] = fill
                queue.append((next_x, next_y))


# Example usage
if __name__ == "__main__":
    matrix = [
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1']
    ]

    print("Before flood fill:")
    for row in matrix:
        print(' '.join(row))

    flood_fill(matrix, 1, 1, '2', ['1'])

    print("\nAfter flood fill:")
    for row in matrix:
        print(' '.join(row))

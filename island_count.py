"""
O(r * c) time
O(r * c) space

r = rows
c = cols
"""


def island_count(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) is True:
                count += 1

    return count


def explore(grid, r, c, visited):
    row_in_bounds = 0 <= r < len(grid)
    col_in_bounds = 0 <= c < len(grid[0])
    if not row_in_bounds or not col_in_bounds:
        return False

    if grid[r][c] == 'W':
        return False

    pos = (r, c)
    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

grid1 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

grid2 = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

print(island_count(grid))
print(island_count(grid1))
print(island_count(grid2))

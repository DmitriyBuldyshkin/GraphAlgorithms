def min_island(grid):
    visited = set()
    min_size = float('inf')

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if 0 < size < min_size:
                min_size = size
    return min_size


def explore_size(grid, r, c, visited):
    row_in_bounds = 0 <= r < len(grid)
    col_in_bounds = 0 <= c < len(grid[0])
    if not row_in_bounds or not col_in_bounds:
        return 0

    if grid[r][c] == 'W':
        return 0

    pos = (r, c)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += explore_size(grid, r - 1, c, visited)
    size += explore_size(grid, r + 1, c, visited)
    size += explore_size(grid, r, c - 1, visited)
    size += explore_size(grid, r, c + 1, visited)
    return size


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

grid1 = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(min_island(grid))
print(min_island(grid1))

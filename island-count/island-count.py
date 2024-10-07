def islandCount(island: list[list]) -> int:
    res = 0
    visited = set()

    for row in range(0, len(island)):
        for col in range(0, len(island[row])):
            if dfs(island, row, col, visited):
                res += 1

    return res


def dfs(grid: list[list], row: int, col: int, visited: set = None) -> bool:
    if visited is None:
        visited = set()
    if (row, col) in visited:
        return False
    if row < 0 or col < 0:
        return False
    if row > len(grid) - 1 or col > len(grid[row]) - 1:
        return False
    if grid[row][col] != "l":
        return False
    
    visited.add((row, col))

    # visit the neighbors
    dfs(grid, row, col - 1, visited)    # left
    dfs(grid, row, col + 1, visited)    # right
    dfs(grid, row - 1, col, visited)    # up
    dfs(grid, row + 1, col, visited)    # down

    return True

def main():
    grid = [
        ["w", "l", "w", "w", "w"],
        ["w", "l", "w", "w", "w"],
        ["w", "w", "w", "l", "w"],
        ["w", "w", "l", "l", "w"],
        ["l", "w", "w", "l", "l"],
        ["l", "l", "w", "w", "w"],
    ]

    print(islandCount(grid)) # 3


if __name__ == "__main__":
    main()
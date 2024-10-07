import sys

def minIsland(island: list[list]) -> int:
    minCount = sys.maxsize
    visited = set()

    for row in range(0, len(island)):
        for col in range(0, len(island[row])):
            if island[row][col] == "l":
                currentCount = dfs(island, row, col, visited)
                if currentCount > 0 and minCount > currentCount:
                    minCount = currentCount
    
    return minCount

def dfs(grid: list[list], row: int, col: int, visited: set = None) -> int:
    if visited is None:
        visited = set()
    if row < 0 or col < 0:
        return 0
    if row > len(grid) - 1 or col > len(grid[row]) - 1:
        return 0
    if (row, col) in visited:
        return 0
    if grid[row][col] != "l":
        return 0
    
    count = 1
    visited.add((row, col))

    count += dfs(grid, row, col - 1, visited)
    count += dfs(grid, row, col + 1, visited)
    count += dfs(grid, row - 1, col, visited)
    count += dfs(grid, row + 1, col, visited)

    return count

def main():
    grid = [
        ["w", "l", "w", "w", "w"],
        ["w", "l", "w", "w", "w"],
        ["w", "w", "w", "l", "w"],
        ["w", "w", "l", "l", "w"],
        ["l", "w", "w", "l", "l"],
        ["l", "l", "w", "w", "w"],
    ]

    print(minIsland(grid)) # 2


if __name__ == "__main__":
    main()
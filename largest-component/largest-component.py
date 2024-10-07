def largestComponent(graph: dict) -> int:
    longestComponentSize = 0
    visited = set()

    for node in graph:
        currentComponentSize = dfsr(graph, node, visited)
        # currentComponentSize = dfs(graph, node, visited)
        if longestComponentSize < currentComponentSize:
            longestComponentSize = currentComponentSize

    return longestComponentSize

def dfs(graph: dict, src: int, visited: set = None) -> int:
    if visited is None:
        visited = set()

    if src in visited:
        return 0
    
    count = 0
    stack = [src]
    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        count += 1
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    
    return count

def dfsr(graph: dict, src: int, visited: set = None) -> int:
    if visited is None:
        visited = set()
    
    if src in visited:
        return 0
    
    count = 1
    visited.add(src)
    for neighbor in graph[src]:
        count += dfsr(graph, neighbor, visited)

    return count


def main():
    graph = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }

    print(largestComponent(graph)) # 5


if __name__ == "__main__":
    main()
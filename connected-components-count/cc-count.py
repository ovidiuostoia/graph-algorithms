def cc_count(graph: dict) -> int:
    visited = set()
    count = 0

    for node in graph:
        # if bfs(graph, node, visited):
        if dfs(graph, node, visited):
            count += 1

    return count

def dfs(graph: dict, src: int, visited: set = None) -> bool:
    if visited is None:
        visited = set()
    if src in visited:
        return False
    
    visited.add(src)
    for neighbor in graph[src]:
        dfs(graph, neighbor, visited)

    return True

def bfs(graph: dict, src: str, visited: set = None) -> bool:
    if src in visited:
        return False
    
    queue = [src]
    while len(queue) > 0:
        current = queue.pop(0)
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return True

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

    print(cc_count(graph)) # 3

if __name__ == "__main__":
    main()
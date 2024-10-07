def edgesToAdjencyList(edges: list) -> dict:
    graph = {}

    for edge in edges:
        m, n = edge

        if m not in graph:
            graph[m] = []
        if n not in graph:
            graph[n] = []

        graph[m].append(n)
        graph[n].append(m)

    return graph

def shortestPath(graph: dict, src: str, dest: str) -> int:
    visited = set()
    queue = [(src, 0)] # tuple of format (node, distance)
    while len(queue) > 0:
        current, distance = queue.pop(0)
        visited.add(current)

        if current == dest:
            return distance
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return -1


def main():
    edges = [
        ["w", "x"],
        ["x", "y"],
        ["z", "y"],
        ["z", "v"],
        ["w", "v"],
    ]

    graph = edgesToAdjencyList(edges)
    # for node in graph:
    #     print(f"{node}: {graph[node]}")

    print(shortestPath(graph, "w", "z")) # 2
    print(shortestPath(graph, "w", "a")) # -1


if __name__ == "__main__":
    main()
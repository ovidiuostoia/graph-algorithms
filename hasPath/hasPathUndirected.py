def edgesToAdjencyList(edges: list) -> dict:
    graph = {}

    for edge in edges:
        key, value = edge

        if key not in graph:
            graph[key] = []

        if value not in graph:
            graph[value] = []

        graph[key].append(value)
        graph[value].append(key)

    return graph

def hasPathUndirectedDFS(graph: dict, src: str, dest: str) -> bool:
    stack = [src]
    visited = set()

    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        if current == dest:
            return True
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)

    return False

def hasPathUndirectedDFSRecursive(graph: dict, src: str, dest: str, visited: set = None) -> bool:
    if visited == None:
        visited = set()
    if src == dest:
        return True
    if src in visited:
        return False
    
    visited.add(src)
    for neighbor in graph[src]:
        if hasPathUndirectedDFSRecursive(graph, neighbor, dest, visited):
            return True

    return False

def hasPathUndirectedBFS(graph: dict, str: str, dest: str) -> bool:
    queue = [str]
    visited = set()

    while len(queue) > 0:
        current = queue.pop(0)
        visited.add(current)

        if current == dest:
            return True
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False

def main():
    edges = [
        ["i", "j"],
        ["k", "i"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"]
    ]
    
    graph = edgesToAdjencyList(edges)
    # for node, neighbors in graph.items():
    #     print(f"{node}: {neighbors}")

    print(hasPathUndirectedDFS(graph, "i", "j")) # True
    print(hasPathUndirectedDFS(graph, "i", "n")) # False

    print(hasPathUndirectedDFSRecursive(graph, "i", "j")) # True
    print(hasPathUndirectedDFSRecursive(graph, "i", "n")) # False



if __name__ == "__main__":
    main()
def hasPathDFS(graph: dict, src: str, dest: str) -> bool:
    stack = [src]

    while len(stack) > 0:
        current  = stack.pop()
        if current == dest:
            return True
        
        for neighbor in graph[current]:
            stack.append(neighbor)

    return False

def hasPathDFSRecursive(graph: dict, src: str, dest: str) -> bool:
    if src == dest:
        return True
    
    for neighbor in graph[src]:
        if (hasPathDFSRecursive(graph, neighbor, dest)):
            return True
    
    return False

def hasPathBFS(graph: dict, src: str,  dest: str) -> bool:
    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == dest:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)

    return False

def get_graph():
    graph = {
        "f": ["g", "i"],
        "g": ["h"],
        "h": [],
        "i": ["g", "k"],
        "j": ["i"],
        "k": []
    }
    return graph

def main():
    graph = get_graph()

    print(hasPathDFS(graph, "f", "k")) # True
    print(hasPathDFS(graph, "f", "j")) # False

    print(hasPathDFSRecursive(graph, "f", "k")) # True
    print(hasPathDFSRecursive(graph, "f", "j")) # False

    print(hasPathBFS(graph, "f", "k")) # True
    print(hasPathBFS(graph, "f", "j")) # False

if __name__ == "__main__":
    main()
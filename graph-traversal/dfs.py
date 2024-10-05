def depthFirstPrint(graph: dict, source: str) -> None:
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

def depthFirstPrintRecursive(graph: dict, source: str) -> None:
    print(source)
    for neighbor in graph[source]:
        depthFirstPrintRecursive(graph, neighbor)

def get_graph():
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    return graph

def main():
    graph = get_graph()
    depthFirstPrint(graph, "a") # a, c, e, b, d, f
    depthFirstPrintRecursive(graph, "a") # a, c, e, b, d, f


if __name__ == "__main__":
    main()
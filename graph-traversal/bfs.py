import queue as q

def breadthFirstPrint(graph: dict, source: str) -> None:
    queue = q.Queue()
    queue.put(source)

    while not queue.empty():
        current = queue.get()
        print(current)

        for neighbor in graph[current]:
            queue.put(neighbor)

def breadthFirstAsArrayPrint(graph: dict, source: str) -> None:
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0) # pops the first element
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)

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
    breadthFirstPrint(graph, "a") # a, b, c, d, e, f
    breadthFirstAsArrayPrint(graph, "a") # a, b, c, d, e, f


if __name__ == "__main__":
    main()
# graph-algorithms

Graph Algorithms Course for Technical Interviews
https://www.youtube.com/watch?v=2_Uuixtc5i0

- a graph is a collection of `nodes` (or vertex) and `edges`
- an `edge` is a connection between `two nodes`
- graphs can be `directed` or `undirected`
- the most preferred way to represent graph information is through an `adjency list` which is just a map with a node as a key and a list of nodes as a value for that key.
- a graph is called `acyclic` if it has no cycles, this means that it doesn't have infinite cycles.

```python
# adjency list graph example
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": [],
    "e": ["b"],
    "f": ["d"]
}

# edges list graph example
edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"],
]
```

## Graph traversal

### Depth-First Search
- it uses a stack
- searches in one direction as much as possible, then backtracks
- can be implemented in an iterative or recursive way

### Breadth-First Search
- it uses a queue
- searches evenly in all directions
- it is implemented in an iterative way
- in an unweighted graph, BFS always returns the shortest path between two nodes
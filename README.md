# graph-algorithms

Graph Algorithms Course for Technical Interviews
https://www.youtube.com/watch?v=2_Uuixtc5i0

- a graph is a collection of `nodes` (or vertex) and `edges`
- an `edge` is a connection between `two nodes`
- graphs can be `directed` or `undirected`
- the most preferred way to represent graph information is through an `adjency list` which is just a map with a node as a key and a list of nodes as a value for that key.

```python
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": [],
    "e": ["b"],
    "f": ["d"]
}
```

## Graph traversal

### Depth-First Search
- it uses a stack
- searches in one direction as much as possible, then backtracks

### Breadth-First Search
- it uses a queue
- searches evenly in all directions
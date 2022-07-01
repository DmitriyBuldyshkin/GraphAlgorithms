def shortest_path(edges, node_a, node_b):
    graph = build_graph(edges)
    visited = {node_a}
    queue = [[node_a, 0]]

    while len(queue) > 0:
        [node, distance] = queue.pop(0)

        if node == node_b:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])

    return -1


def build_graph(edges):
    graph = {}
    for edge in edges:
        [a, b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

edges2 = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]

print(shortest_path(edges, 'w', 'z'))
print(shortest_path(edges2, 'b', 'g'))

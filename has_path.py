def has_path(graph, src, dst):
    """
    n = number of nodes
    e or n ^ 2= number of edges

    O(e) or O(n ^ 2) time
    O(n) space
    """
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) is True:
            return True

    return False


def has_path1(graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)

        if current == dst:
            return True

        for neighbor in graph[current]:
            queue.append(neighbor)

    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path(graph, 'f', 'k'))
print(has_path1(graph, 'f', 'k'))

def depth_first(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


def depth_first_rec(graph, source):
    print(source)
    for neighbor in graph[source]:
        depth_first_rec(graph, neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first(graph, 'a')
print(" ")
depth_first_rec(graph, 'a')

import random


def bfs(graph, start_node):
    visited = []  # List to track visited nodes
    queue = [start_node]  # Queue to manage the traversal

    print("BFS Traversal:")
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, end=" ")
            visited.append(current)

            # Shuffle the neighbors to add randomness
            neighbors = list(graph[current])
            random.shuffle(neighbors)
            queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)


# Example graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'G'],
    'E': ['B'],
    'F': ['C'],
    'G': ['D']
}
bfs(graph, 'A')

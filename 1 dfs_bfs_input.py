from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Get user input
g = Graph()
num_edges = int(input("Enter number of edges: "))

print("Enter each edge in the format 'u v':")
for _ in range(num_edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start_node = int(input("Enter starting node for traversal: "))

print("\nDFS Recursive starting from vertex", start_node, ":")
g.dfs_recursive(start_node)

print("\nBFS starting from vertex", start_node, ":")
g.bfs(start_node)

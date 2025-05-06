from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Since the graph is undirected, add both edges
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


# Example Usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)

print("DFS Recursive starting from vertex 0:")
g.dfs_recursive(0)

print("\nBFS starting from vertex 0:")
g.bfs(0)
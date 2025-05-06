# Define the graph structure
Graph_nodes = {
    'A': [('B', 2), ('C', 2),('H',7)],
    'B': [('D', 4), ('E', 6)],
    'C': [('F', 3), ('G', 2)],
    'F': [('H', 1)],
    'G': [('H', 2)],
}

def aStarAlgo(start_node, stop_node):
    open_set = {start_node}  # This should be a set containing start_node
    closed_set = set()
    g = {}  # Store distance from the starting node
    parents = {}  # Parents contains an adjacency map of all nodes
    g[start_node] = 0
    parents[start_node] = start_node
    
    while len(open_set) > 0:
        n = None
        # Find node with the lowest f() value
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # If the node is the stop_node or has no neighbors
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        if Graph_nodes.get(n) is None:
            print('Path does not exist!')
            return None

        # Evaluate the neighbors
        for (m, weight) in get_neighbors(n):
            # If the neighbor m is not in open_set or closed_set
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # Move n from open_set to closed_set
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


# Define function to return neighbors and their distances from a node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []


# Define the heuristic function with estimated distances to the goal node
def heuristic(n):
    H_dist = {
        'A': 13,
        'B': 12,
        'C': 4,
        'D': 7,
        'E': 3,
        'F': 8,
        'G': 2,
        'H': 0
    }
    return H_dist[n]

# Running the A* algorithm from 'A' to 'H'
aStarAlgo('A', 'H')



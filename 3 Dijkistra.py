import heapq

def djikstras(graph, start, end):
    pq = [(0, start)]  # Priority queue stores (cost so far, current node)
    visited = set()    # To avoid revisiting nodes

    while pq:
        (cost, curr_node) = heapq.heappop(pq)  # Node with least cost is picked

        if curr_node == end:
            return cost  # If we reached the destination

        if curr_node in visited:
            continue  # Skip if already visited

        visited.add(curr_node)

        for (next_node, edge_cost) in graph[curr_node]:
            if next_node not in visited:
                heapq.heappush(pq, (cost + edge_cost, next_node))  # Add neighbor with updated cost

    return float("inf")  # If no path is found

# Define the graph
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

# Run the algorithm
shortest_distance = djikstras(graph, 'B', 'D')
print("The shortest Distance between B and D is", shortest_distance)





# --------------------- USER INPUT SECTION ---------------------
# graph = {}
# n = int(input("Enter number of nodes: "))
# for _ in range(n):
#     node = input(f"Enter name of node #{_+1}: ")
#     graph[node] = []

# e = int(input("Enter number of edges: "))
# print("Enter edges in the format: from_node to_node cost")
# for _ in range(e):
#     u, v, cost = input().split()
#     cost = int(cost)
#     graph[u].append((v, cost))
#     graph[v].append((u, cost))  # Remove this line if the graph is directed

# start = input("Enter start node: ")
# end = input("Enter end node: ")

# --------------------- RUN THE ALGORITHM ---------------------
# shortest_distance = djikstras(graph, start, end)
# print("The shortest Distance between", start, "and", end, "is", shortest_distance)
graph = {
'5' : ['3', '7'],
'3' : ['2', '4'],
'7' : ['8'],
'4' : ['8'],
'2' : [],
'8' : []
}

visited = set()  

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(visited, graph, neighbour)

print("The dfs is :")
dfs(visited, graph, '5')

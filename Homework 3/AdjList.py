from collections import deque

def buildAdjList(edges):
    AdjacencyList = {}
    for item in edges:
        if item[0] not in AdjacencyList:
            AdjacencyList[item[0]] = []
        if item[1] not in AdjacencyList:
            AdjacencyList[item[1]] = []
        AdjacencyList[item[0]].append(item[1])
    return AdjacencyList
    
def print_graph(graph):
    for key in graph:
        print(str(key) + " = " + str(graph[key]))
    
def bfs(target, graph):
    visited = {}
    for vertex in graph:
        visited[vertex] = False
    queue = deque()
    queue.append(list(graph.keys())[0])
    while queue:
        cur_vertex = queue.popleft()
        if cur_vertex == target:
            return True
        for edge in graph[cur_vertex]:
            if not visited[edge]:
                queue.append(edge)
                visited[edge] = True
    return False

def dfs(target, graph):
    visited = {}
    for vertex in graph:
        visited[vertex] = False
    stack = []
    stack.append(list(graph.keys())[0])
    while stack:
        cur_vertex = stack.pop()
        if cur_vertex == target:
            return True
        if not visited[cur_vertex]:
            visited[cur_vertex] = True
            stack.extend(graph[cur_vertex])
    return False

def topological_sort(graph):
    in_degree = {}
    for vertex in graph:
        in_degree[vertex] = in_degree.get(vertex,0)
        for edge in graph[vertex]:
            in_degree[edge] = in_degree.get(edge,0) + 1
    res = []
    queue = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            queue.append(key)
    while queue:
        cur_vertex = queue.popleft()
        res.append(cur_vertex)
        for edge in graph[cur_vertex]:
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                queue.append(edge)
    return res
        

if __name__ == "__main__":
    adj = buildAdjList([(1,2),(1,3),(2,3),(3,1), (1,0)])
    assert bfs(2,adj) == True
    assert bfs(3,adj) == True
    assert bfs(4,adj) == False
    assert bfs(0,adj) == True
    assert bfs(5,adj) == False

    assert dfs(2,adj) == True
    assert dfs(3,adj) == True
    assert dfs(4,adj) == False
    assert dfs(0,adj) == True
    assert dfs(5,adj) == False

    new_adj = buildAdjList([(5, 2), (5, 0), (4, 0),(4, 1),(2, 3),(3, 1)])
    assert topological_sort(new_adj) == [5, 4, 2, 0, 3, 1]

    print("Testing Complete")



    
        
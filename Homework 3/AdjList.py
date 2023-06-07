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

        
        


if __name__ == "__main__":
    aj = buildAdjList([(1,2),(1,3),(2,3),(3,1), (1,0)])
    print_graph(aj)
    assert bfs(2,aj) == True
    assert bfs(3,aj) == True
    assert bfs(4,aj) == False
    assert bfs(0,aj) == True
    assert bfs(5,aj) == False

    assert dfs(2,aj) == True
    assert dfs(3,aj) == True
    assert dfs(4,aj) == False
    assert dfs(0,aj) == True
    assert dfs(5,aj) == False

    print("Testing Complete")



    
        
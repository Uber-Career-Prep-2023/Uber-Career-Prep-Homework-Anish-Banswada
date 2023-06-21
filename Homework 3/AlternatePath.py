# Name : Anish Banswada

# Time Taken : 35 mins

# Assumptions : None

# Space Complexity : O(V + E)

# Time Complexity : O(V + E)

# Function 
def pathFinder(connections, origin, destination):
    graph = {}
    for connection in connections:
        graph[connection[0]] = graph.get(connection[0],[]) + [(connection[1], connection[2])]
    length = []
    for vertex in graph[origin]:
        dfs(graph, vertex, destination, 1, length)
    if not length:
        return -1
    return min(length)

def dfs(graph, cur_vertex, destination, cur_length,length):
    if cur_vertex[0] == destination:
        length.append(cur_length)
        return
    if graph[cur_vertex[0]]:
        for vertex in graph[cur_vertex[0]]:
            if vertex[1] != cur_vertex[1]:
                dfs(graph, vertex, destination,cur_length + 1, length)

# Main

if __name__ == "__main__":
    assert pathFinder([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")]
, 'A', 'E') == 4
    assert pathFinder([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")]
, 'E', 'D') == -1
    print("Testing completed")
    
   
 
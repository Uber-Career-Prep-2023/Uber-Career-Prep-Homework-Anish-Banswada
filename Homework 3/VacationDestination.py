# Name : Anish Banswada

# Time Taken : 35 mins

# Assumptions : None

# Space Complexity : O(V+E)

# Time Complexity :O(V+E)

# Function 
def vacationDestination(connections, origin, time):
    graph = {}
    visited = {}
    for connection in connections:
        graph[connection[0]] = graph.get(connection[0],[]) + [(connection[1], connection[2])]
        graph[connection[1]] = graph.get(connection[1],[]) + [(connection[0], connection[2])]
        visited[connection[0]] = False
        visited[connection[1]] = False
    visited[origin] = True
    res = []
    for city in graph[origin]:
        if time - city[1] >= 0:
            dfs(graph, city, time - city[1] -1, res, visited)
    return res
def dfs(graph, origin, remaining_time, res, visited):
    visited[origin[0]] = True
    res.append(origin[0])
    if remaining_time <= 0:
        return 
    for city in graph[origin[0]]:
        if not visited[city[0]] and remaining_time - city[1] >= 0:
            dfs(graph, city, remaining_time - city[1] - 1, res, visited)


# Main

if __name__ == "__main__":
    connections = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C", 2.5)]
    assert vacationDestination(connections, "New York", 5) == ['Boston', 'Philadelphia']
    assert vacationDestination(connections, "New York", 7) == ['Boston', 'Newport', 'Philadelphia', 'Washington, D.C']
    assert vacationDestination(connections, "New York", 8) == ['Boston', 'Newport', 'Portland', 'Philadelphia', 'Washington, D.C', "Harper's Ferry"]
    print("Testing completed")

 
# Name : Anish Banswada

# Time Taken : 30 minutes

# Assumptions : None

# Space Complexity : O(V + E)

# Time Complexity : O(V + E)

# Function 
def networks(towns, connections):
    graph = {}
    visited = {}
    for connection in connections:
        graph[connection[0]] = graph.get(connection[0],[]) + [connection[1]]
        visited[connection[0]] = False
        visited[connection[1]] = False
        graph[connection[1]] = graph.get(connection[1],[]) + [connection[0]]
    count = 0
    for town in graph:
        if not visited[town]:
            dfs(graph, town, visited)
            count += 1
    return count
def dfs(graph, town, visited):
    if not visited[town]:
        visited[town] = True
    for connection in graph[town]:
        if not visited[connection]:
            dfs(graph, connection, visited)
    return 

# Main

if __name__ == "__main__":
    assert networks(["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"], 
[("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
) == 2
    assert networks(["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), 
    ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]) == 3
   
 
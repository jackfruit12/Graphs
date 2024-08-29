from collections import deque, defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)
    
    def bfs_from_hospitals(self, hospital_towns):
        # Initialize distances with infinity for all nodes
        distance = {i: float('inf') for i in range(1, n + 1)}
        
        # Initialize the queue with all hospital towns
        queue = deque(hospital_towns)
        for town in hospital_towns:
            distance[town] = 0
        
        while queue:
            current_node = queue.popleft()
            
            for neighbor in self.adj_list[current_node]:
                if distance[neighbor] == float('inf'):  # Unvisited node
                    distance[neighbor] = distance[current_node] + 1
                    queue.append(neighbor)
        
        return distance

# Example usage:
if __name__ == "__main__":
    g = Graph()
    n, m = map(int, input().split())
    hospitals = list(map(int, input().split()))
    
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)
    
    # Get the list of towns that have hospitals
    hospital_towns = [i + 1 for i in range(n) if hospitals[i] == 1]
    
    # If no town has a hospital, return -1
    if not hospital_towns:
        print(-1)
    else:
        # Perform BFS from all hospital towns
        distances = g.bfs_from_hospitals(hospital_towns)
        
        # Find the maximum distance from any town to its nearest hospital
        max_distance = max(distances[i] for i in range(1, n + 1))
        
        # If any town is unreachable, return -1
        if max_distance == float('inf'):
            print(-1)
        else:
            print(max_distance)
'''
Given N
 towns and M
 bidirectional roads. Travelling across each road takes exactly 1 day.

Find out maximal possible time you will need to travel if you start from some town and want to reach nearest city which has a hospital.

If there is a town, from which you cannot reach to a city with hospital then print "-1"

Input
The first line contains two integers N
 and M
, the number of towns and the number of bidirectional roads respectively.
The second line contains N
 integers, where each integer is either 0 (city has no hospital), 1 (city has a hospital) representing the presence of an hospital in each town.
The next M
 lines each contain two integers u
 and v
, representing a bidirectional road between towns u
 and v
.
Output
Single integer representing maximal possible time you will need to travel if you start from some town and want to reach nearest city which has a hospital or "-1" if a town is unreachable by any hospital city.

Examples
Input
6 5
1 0 0 0 0 1
1 2
2 3
3 4
1 5
5 6
Output
3
Input
4 2
1 1 0 0
1 2
3 4
Output
-1
Input
4 2
1 0 0 1
1 2
3 4
Output
1
'''

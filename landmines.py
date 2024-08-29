from collections import deque, defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)
    
    def bfs(self, start):
        # Dictionary to store distance from start node
        distance = {node: float('inf') for node in self.adj_list}
        distance[start] = 0
        
        queue = deque([start])
        
        while queue:
            current_node = queue.popleft()
            
            for neighbor in self.adj_list[current_node]:
                if distance[neighbor] == float('inf'):  # Unvisited node
                    distance[neighbor] = distance[current_node] + 1
                    queue.append(neighbor)
        
        return distance
    
    def print_graph(self):
        for key, value in self.adj_list.items():
            print(f"{key}: {value}")

# Example usage:
if __name__ == "__main__":
    g = Graph(directed=False)
    n,m=map(int,input().split())
    s,t=map(int,input().split())
    e=list(map(int,input().split()))
    for i in range(m):
      u,v=map(int,input().split())
      if e[u]!=1 and e[v]!=1:
        g.add_edge(u,v)
        # g.add_edge(v,u)
    
    l = g.bfs(s)
    
    if(l.get(t) == float("inf")) or (l.get(t)==None):
      print(-1)
    else:
      print(l.get(t))
'''
There are N
 cities with M
 bi-directional roads between them. You want to travel from a given source city to target city. But there are some cities that have landmines in them and you will die if you visit these cities.

Find the smallest number of roads that you can take to complete your travel without dying. If it is not possible to do so output −1
.

Input
The first line contains two integers N
 and M
 denoting the number of cities and the number of roads respectively.

The second line contains two integers: source and target.

The third line contains N
 integers which are either 0
 or 1
 denoting whether each city has landmines or not. (1
 means that the city has landmines.)

Finally, there are M
 lines containing 2
 integers each u
 and v
 denoting that there is a road between city u
 and city v
.

Output
Output the smallest number of roads that you should take to complete your travel without dying. If it is not possible to do so output −1
.

Example
Input
5 5
0 2
0 1 0 0 0
0 1
1 2
0 3
3 4
4 2
Output
3
'''

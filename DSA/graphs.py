class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            #self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
            
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size

        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)
        
    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
        
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=' ')
            
            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    graph = Graph(7)

    vertex_set = [(num, string) for num, string in zip(range(7), "ABCDEFG")]
    for data in vertex_set:
        graph.add_vertex_data(data[0], data[1])

    graph.add_edge(3, 0)  
    graph.add_edge(3, 4)  
    graph.add_edge(4, 0)  
    graph.add_edge(0, 2)  
    graph.add_edge(2, 5)  
    graph.add_edge(2, 6)  
    graph.add_edge(5, 1)  
    graph.add_edge(1, 2)  

    graph.print_graph()

    print("\nDepth First Search starting from vertex D:")
    graph.dfs('D')

    print("\n\nBreadth First Search starting from vertex D:")
    graph.bfs('D')

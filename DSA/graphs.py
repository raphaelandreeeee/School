class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency_list = dict()

    def __repr__(self):
        graph = ""

        for node, neighbors in self.adjacency_list:
            graph += f"{node}: {neighbors}\n"

        return graph

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = set()
        else:
            raise ValueError("Node already exists.")

    def remove_node(self, node):
        if node not in self.adjacency_list:
            raise ValueError("Node does not exists.")
        else:
            for neighbors in self.adjacency_list.values():
                neighbors.discard(node)

            del self.adjacency_list[node]

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adjacency_list:
            raise ValueError("Node does not exists.")
        
        if to_node not in self.adjacency_list:
            raise ValueError("Node does not exists.")
        
        if weight is None:
            self.adjacency_list[from_node].add(to_node)

            if not self.directed:
                self.adjacency_list[to_node].add(from_node)

        else:
            self.adjacency_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adjacency_list[to_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        if from_node in self.adjacency_list:
            if to_node in self.adjacency_list[from_node]:
                self.adjacency_list[from_node].remove(to_node)
            else:
                raise ValueError("Edge does not exists.")
        else:
            raise ValueError("Node does not exists.")

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, set())

    def has_node(self, node):
        return node in self.adjacency_list

    def has_edge(self,from_node, to_node):
        if from_node in self.adjacency_list:
            return to_node in self.adjacency_list[from_node]
        return False
    
    def get_nodes(self): 
        return list(self.adjacency_list.keys())
    
    def get_edges(self):
        return [(from_node, to_node) for from_node, neighbors in self.adjacency_list.items() for to_node in neighbors]

    def bfs(self, node):
        pass

    def dfs(self, node):
        pass


if __name__ == '__main__':
    graph = Graph()

    graph.add_node()
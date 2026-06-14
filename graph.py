from collections import deque
from inspect import stack
from tracemalloc import start
class GraphAdjacencyList:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            print(f"  Vertex '{vertex}' ditambahkan.")
        else:
            print(f"  Vertex '{vertex}' sudah ada.")
    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        if not self.directed:
            self.adjacency_list[v].append(u)
    def remove_edge(self, u, v):
        """Menghapus edge antara dua vertex."""
        if u in self.adjacency_list:
            self.adjacency_list[u] = [
                vertex for vertex in self.adjacency_list[u] if vertex != v
            ]
        if not self.directed and v in self.adjacency_list:
            self.adjacency_list[v] = [
                vertex for vertex in self.adjacency_list[v] if vertex != u
            ]
        print(f"  Edge '{u}' -- '{v}' dihapus.")
    def remove_vertex(self, vertex):
        """Menghapus vertex beserta semua edge yang terhubung."""
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v in self.adjacency_list:
                self.adjacency_list[v] = [
                    u for u in self.adjacency_list[v] if u != vertex
                ]
            print(f"  Vertex '{vertex}' dihapus.")
    def display(self):
        """Menampilkan adjacency list."""
        print("\n  === Adjacency List ===")
        for vertex, neighbors in self.adjacency_list.items():
            print(f"  {vertex} -> {neighbors}")
    # ----------------------------------------
    # BREADTH-FIRST SEARCH (BFS)
    # ----------------------------------------
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = [] 
        visited.add(start)
        print(f"\n  === BFS dimulai dari vertex '{start}' ===")
        print(f"  {'Step':<6} {'Queue':<30} {'Dikunjungi'}")
        print(f"  {'-'*60}")
        step = 1
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            print(f"  {step:<6} {str(list(queue)):<30} {sorted(visited)}")
            step += 1
            print(vertex)  # Process the vertex
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
    # ----------------------------------------
    # DEPTH-FIRST SEARCH (DFS)
    # ----------------------------------------
    def dfs(self, start, visited=None, result=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []
        visited.add(start)
        result.append(start)
        print(start)  # Process the vertex
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)
        return result
    def dfs_recursive(self, start):
        visited = set()
        result = []
        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
        print(f"\n  === DFS (Recursive) dimulai dari vertex '{start}' ===")
        dfs_helper(start)
        print(f"  Hasil DFS (Rekursif): {result}")
        return result
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in reversed(self.adjacency_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result
class GraphAdjacencyMatrix:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.vertex_index = {v: i for i, v in enumerate(vertices)}
        self.n = len(vertices)
        self.adjacency_matrix = [[0] * self.n for _ in range(self.n)]
        self.directed = directed
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * len(self.vertices))
            print(f"  Vertex '{vertex}' ditambahkan.")
        else:
            print(f"  Vertex '{vertex}' sudah ada.")
    def add_edge(self, u, v, weight=1):
        if u  not in self.vertex_index or v not in self.vertex_index:
            print(f"  Vertex '{u}' or '{v}' tidak ditemukan.")
        else:
            index_u = self.vertex_index[u]
            index_v = self.vertex_index[v]
            self.adjacency_matrix[index_u][index_v] = weight
            if not self.directed:
                self.adjacency_matrix[index_v][index_u] = weight
    def remove_edge(self, u, v):
        """Menghapus edge antara dua vertex."""
        if u not in self.vertex_index or v not in self.vertex_index:
            return
        i = self.vertex_index[u]
        j = self.vertex_index[v]
        self.adjacency_matrix[i][j] = 0
        if not self.directed:
            self.adjacency_matrix[j][i] = 0
        print(f"  Edge '{u}' -- '{v}' dihapus.")
    def remove_vertex(self, vertex):
        """Menghapus vertex beserta semua edge yang terhubung."""
        if vertex not in self.vertex_index:
            return
        index = self.vertex_index[vertex]
        # Hapus baris dan kolom dari matriks
        self.adjacency_matrix.pop(index)
        for row in self.adjacency_matrix:
            row.pop(index)
        # Hapus vertex dari daftar dan indeks
        self.vertices.remove(vertex)
        del self.vertex_index[vertex]
        # Update indeks vertex yang tersisa
        for i, v in enumerate(self.vertices):
            self.vertex_index[v] = i
        print(f"  Vertex '{vertex}' dihapus.")
    def has_edge(self, u, v):
        """Mengecek apakah ada edge antara dua vertex."""
        i = self.vertex_index[u]
        j = self.vertex_index[v]
        return self.adjacency_matrix[i][j] != 0
    def display(self):
        print("\n  === Adjacency Matrix ===")
        print("    " + " ".join(f"{v:>3}" for v in self.vertices))
        for i, vertex in enumerate(self.vertices):
            row = " ".join(f"{self.adjacency_matrix[i][j]:>3}" for j in range(len(self.vertices)))
            print(f"  {vertex:>3} {row}")
    # ----------------------------------------
    # BFS menggunakan Adjacency Matrix
    # ----------------------------------------
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = [] 
        visited.add(start)
        print(f"\n  === BFS dimulai dari vertex '{start}' ===")
        print(f"  {'Step':<6} {'Queue':<30} {'Dikunjungi'}")
        print(f"  {'-'*60}")
        step = 1
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            print(f"  {step:<6} {str(list(queue)):<30} {sorted(visited)}")
            step += 1
            print(vertex)  # Process the vertex
            for neighbor in self.vertices:
                if self.has_edge(vertex, neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
    # ----------------------------------------
    # DFS menggunakan Adjacency Matrix
    # ----------------------------------------
    def dfs(self, start, visited=None, result=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []
        visited.add(start)
        result.append(start)
        stack = [start]
        while stack:
            idx = stack.pop()
            if idx not in visited:
                visited.add(idx)
                result.append(self.vertices[idx])
 
                for j in range(self.n - 1, -1, -1):
                    if self.matrix[idx][j] != 0 and not visited[j]:
                        stack.append(j)
 
        print(f"  Hasil DFS: {result}")
        return result
# ============================================================
# MAIN - DEMONSTRASI SEMUA FITUR
# ============================================================
if __name__ == "__main__":
    print("=== Graph dengan Adjacency List ===")
    graph_list = GraphAdjacencyList(directed=False)
    graph_list.add_vertex('A')
    graph_list.add_vertex('B')
    graph_list.add_vertex('C')
    graph_list.add_edge('A', 'B')
    graph_list.add_edge('A', 'C')
    graph_list.add_edge('B', 'C')
    graph_list.display()
    bfs_result = graph_list.bfs('A')
    print(f"Hasil BFS: {bfs_result}")
    dfs_result = graph_list.dfs('A')
    print(f"Hasil DFS: {dfs_result}")
    print("\n=== Graph dengan Adjacency Matrix ===")
    vertices = ['A', 'B', 'C']
    graph_matrix = GraphAdjacencyMatrix(vertices, directed=False)
    graph_matrix.add_edge('A', 'B')
    graph_matrix.add_edge('A', 'C')
    graph_matrix.add_edge('B', 'C')
    graph_matrix.display()
    bfs_result_matrix = graph_matrix.bfs('A')
    print(f"Hasil BFS: {bfs_result_matrix}")
    dfs_result_matrix = graph_matrix.dfs('A')   
    print(f"Hasil DFS: {dfs_result_matrix}")
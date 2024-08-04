# Define the graph class
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to store the graph

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []  # Initialize an empty list for the vertex
            print(self.graph)

    def add_edge(self, vertex1, vertex2):
        # Ensure both vertices exist in the graph
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        # Add the edge
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# Create a graph object
g = Graph()

# Add edges using a loop
n = 3
for i in range(n):
    vertex1 = input('enter vertax1: ')
    vertex2 = input('enter vertax2: ')

    g.add_edge(vertex1, vertex2)

# Display the graph
g.display()

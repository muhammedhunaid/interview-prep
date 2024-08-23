from __future__ import annotations
from graph_adj_list import *


def _dfs(graph: GraphAdjList[any], vertex: any, visited: set[any]) -> None:
    #if dfs is called from outside, it will print the vertex
    print(vertex)
    #if dfs is called from inside, it will add the vertex to visited set
    visited.add(vertex)
    #for each neighbor of the vertex, if the neighbor is not visited, call dfs on the neighbor
    neighbor: any
    for neighbor in graph.get_neighbors(vertex):
        if neighbor not in visited:
            _dfs(graph, neighbor, visited)

#dfs function that calls _dfs function for each vertex in the graph
def dfs(graph: GraphAdjList[any]) -> None:
    #initialize visited set
    visited: set[any] = set()
    #for each vertex in the graph, if the vertex is not visited, call _dfs function on the vertex
    vertex: any
    for vertex in graph.get_vertices():
        if vertex not in visited:
            _dfs(graph, vertex, visited)


if __name__ == '__main__':
    #initialize graph where each vertex is connected to its adjacent vertices
    graph: GraphAdjList[any] = GraphAdjList()
    graph.adj_list = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'C': [],
        'D': ['A','H', 'I', 'J'],
        'E': ['B', 'K'],
        'F': ['B', 'L'],
        'H': ['D'],
        'I': ['D', 'O', 'J'],
        'J': ['D', 'I'],
        'K': ['E', 'P', 'L'],
        'L': ['K', 'Q', 'R', 'F'],
        'O': ['I'],
        'P': ['K'],
        'Q': ['L'],
        'R': ['L']
    }

    dfs(graph)

    """Output:
    A
    B
    E
    K
    P
    L
    Q
    R
    F
    C
    D
    H
    I
    O
    J"""
    
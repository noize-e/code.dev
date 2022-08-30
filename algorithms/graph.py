"""
G=(V, E)
    V= vertex set
    E= edge set
"""
from collections import namedtuple


Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])


def adjacency_dict(graph: Graph) -> dict:
    """
    Returns the adjacency list representation
    of the graph.
    """
    adj = {node:[] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj


def adjacency_matrix(graph):
    """
    """
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    return adj


"""
Relationships in graphs
- Undirected graph
- Directed graph
"""
nodes = [0, 1, 2, 3]
edges = [(0,1),
         (0,1),
         (0,2),
         (0,2),
         (0,3),
         (1,3),
         (2,3)]
graph_undirected = Graph(nodes, edges, is_directed=False)
graph_directed = Graph(nodes=range(3), edges=[(1,0), (1,2), (0,2)], is_directed=True)
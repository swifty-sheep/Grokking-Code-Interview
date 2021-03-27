"""
Problem Statement
Topological Sort of a directed graph (a graph with unidirectional edges) is a
linear ordering of its vertices such that for every directed edge (U, V) from
vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:
Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Example 2:
Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1

Example 3:
Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0

There are other valid topological ordering of the graph too.
"""
from collections import deque


def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # a. init the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph
    # b. build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1
    # c. find all sources i.e. all vertices with 0 in-degrees
    sources = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            sources.append(node)
    # d. for each source, add it to the sorted_order and subtract one from all
    # of its children. If a child's in-degree becomes zero, add it to the
    # sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        # get node children to decrement their in-degree
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has cycle
    if len(sorted_order) != vertices:
        return []
    return sorted_order


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7,
                               [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1],
                                [3, 2], [4, 1]])))


main()

if __name__ == "__main__":
    main()

"""
Time Complexity 
In step ‘d’, each vertex will become a source only once and each edge will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E), 
where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.
Space Complexity 
The space complexity will be O(V+E), since we are storing all of the edges for each vertex in an adjacency list.
"""

"""
Similar Problems 
Problem 1: Find if a given Directed Graph has a cycle in it or not.
Solution: If we can’t determine the topological ordering of all the vertices of a directed graph, the graph has a cycle in it. This was also referred to in the above code:
    if (sortedOrder.size() != vertices) // topological sort is not possible as the graph has a cycle
      return new ArrayList<>();
"""

def kruskal(graph_edges):
    sorted_edges = sorted(graph_edges, key=lambda x: x[0])
    parent = {}

    def make_set(vertex):
        parent[vertex] = vertex

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        if root1 != root2:
            parent[root2] = root1


    vertices = set()
    for _, u, v in graph_edges:
        vertices.add(u)
        vertices.add(v)
    for vertex in vertices:
        make_set(vertex)
    mst = []
    for edge in sorted_edges:
        weight, u, v = edge
        if find(u) != find(v):
            mst.append(edge)
            union(u, v)
    return mst

m = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

print(kruskal(m))

# альтернативный, более понятный вывод
print("Ребра минимального остовного дерева:")
for i in kruskal(m):
    print(f"{i[1]} - {i[2]} (вес: {i[0]})")
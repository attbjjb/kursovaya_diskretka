from graphviz import Graph


def kruskal_with_visualization(graph_edges):
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
    step = 1
    visualize_step([], [], "Шаг 1: Начальное состояние", step)
    step += 1

    for edge in sorted_edges:
        weight, u, v = edge
        if find(u) != find(v):
            visualize_step(mst, [edge], f"Шаг {step}: Проверка ребра {u}-{v} (вес {weight})", step)
            step += 1

            mst.append(edge)
            union(u, v)

            visualize_step(mst, [], f"Шаг {step}: Добавлено ребро {u}-{v}", step)
            step += 1
        else:
            visualize_step(mst, [edge], f"Шаг {step}: Пропуск ребра {u}-{v} (образует цикл)", step)
            step += 1
    return mst


def visualize_step(current_mst, processing_edges, title, step_num):
    dot = Graph(comment=title)
    vertices = set()
    for _, u, v in graph_edges:
        vertices.add(u)
        vertices.add(v)
    for vertex in vertices:
        dot.node(str(vertex))
    for edge in graph_edges:
        weight, u, v = edge
        dot.edge(str(u), str(v), label=str(weight), color='gray70', style='dashed')

    for edge in current_mst:
        weight, u, v = edge
        dot.edge(str(u), str(v), label=str(weight), color='green', penwidth='2')

    for edge in processing_edges:
        weight, u, v = edge
        dot.edge(str(u), str(v), label=str(weight), color='red', penwidth='3')

    dot.attr(label=title, labelloc='t', fontsize='20')
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

    filename = f'step_{step_num:02d}'
    dot.render(filename, view=False, format='png')


graph_edges = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
    (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]
mst_edges = kruskal_with_visualization(graph_edges)
visualize_step(mst_edges, [], "Финальный результат: минимальное остовное дерево", 999)
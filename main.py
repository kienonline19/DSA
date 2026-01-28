def dijkstra_pseudocode_style(graph, s):
    """
    Theo mã giả trong slide:
      - d(s)=0; d(u)=inf với u != s
      - R = set() (visited)
      - while R != V:
            pick u not in R with smallest d(u)
            R = R union {u}
            for v adjacent to u:
                if d(v) > d(u) + w(u,v): d(v) = d(u) + w(u,v)

    graph: adjacency list, graph[u] = [(v, w), ...], w >= 0
    return: dist list
    """
    n = len(graph)
    INF = float("inf")

    # for all u in V \ {s}, d(u) = inf; d(s) = 0
    d = [INF] * n
    d[s] = 0

    # R = {}
    R = set()

    # while R != V
    while len(R) != n:
        # pick u not in R with smallest d(u)
        u = None
        best = INF
        for i in range(n):
            if i not in R and d[i] < best:
                best = d[i]
                u = i

        # Nếu phần còn lại đều INF => không còn đỉnh reachable từ s (slide có thể giả sử connected,
        # nhưng để code an toàn ta break)
        if u is None:
            break

        # R = R union {u}
        R.add(u)

        # for all vertices v adjacent to u:
        for v, w in graph[u]:
            if w < 0:
                raise ValueError("Dijkstra yêu cầu trọng số không âm")
            # if d(v) > d(u) + l(u,v)
            if d[v] > d[u] + w:
                # d(v) = d(u) + l(u,v)
                d[v] = d[u] + w

    return d


# ----------------- Test nhanh -----------------
graph = [
    [(1, 4), (2, 1)],     # 0
    [(3, 1)],             # 1
    [(1, 2), (3, 5)],     # 2
    []                    # 3
]
dist = dijkstra_pseudocode_style(graph, 0)
assert dist == [0, 3, 1, 4]

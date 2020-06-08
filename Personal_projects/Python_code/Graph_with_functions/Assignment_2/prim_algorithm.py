def prim(self):
    """ prim's algorithm calculates the minimum spanning tree of the graph
    """
    free = {}  # {vertex: {} }
    for v in self._structure:
        free[v] = {}
    # locs stores location of each vertex in apq
    locs = {}  # { vertex: index }
    pq = APQ_binary_heap()  # contains cost and (vertex, edge) pairs

    for v in self._structure:
        locs[v] = pq.add(math.inf, (v, None))

    output = []
    while pq.length() > 0:
        key, value = pq.remove_min()
        v, e = value[0], value[1]
        del free[v]
        del locs[v]
        if e is not None:
            output.append(e)
        for d in self.get_edges(v):
            w = d.opposite(v)
            cost = d._element
            for x in pq.structure:
                if x._value[0] == w:
                    w_edge = x._value[1]
                    break
            if w in free and cost < pq.get_key((w, w_edge)):
                pq.update_key((w, w_edge), cost)
                pq.update_element((w, w_edge), (w, d))
    return output

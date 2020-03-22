def djikstra(s):
    """ Creates minimum spanning tree from vertex s

    Args:
        s - vertex from where to start the tree
    """
    open = APQ_binary_heap()
    locs = {}
    closed = {}
    preds = {s: None}

    locs[s] = open.add(0, s)
    while open.length() > 0:
        v = open.remove_min()
        del locs[v._value]
        predecessor = preds.pop(v._value)
        closed[v._value] = (v._key, predecessor)
        for e in graph.get_edges(v._value):
            w = e.opposite(v._value)
            if w not in closed:
                newcost = v._key + e._element
                if w not in locs:   # not added in open
                    preds[w] = v._value
                    locs[w] = open.add(newcost, w)
                elif newcost < open.get_key(w):
                    preds[w] = v._value
                    open.update_key(w, newcost)
    return closed
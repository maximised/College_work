def djikstra(self, s):
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
        key, value = open.remove_min()
        del locs[value]
        predecessor = preds.pop(value)
        closed[value] = (key, predecessor)
        for e in self.get_edges(value):
            w = e.opposite(value)
            if w not in closed:
                newcost = key + e._element
                if w not in locs:  # not added in open
                    preds[w] = value
                    locs[w] = open.add(newcost, w)
                elif newcost < open.get_key(w):
                    preds[w] = value
                    open.update_key(w, newcost)
    return closed
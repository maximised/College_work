def mst_kruskal(self):
    """ kruskal finds the minimum spanning tree by joining smaller subtrees from the
        whole tree
    """
    tree = []

    n = self.num_vertices()
    whichtree = {}
    for v in self.vertices():
        vtree = Stack()
        vtree.push(v)
        whichtree[v] = vtree
    pq = APQ_binary_heap()

    for e in self.edges():
        pq.add(e.element(), e)
    while len(tree) < n and pq.length() > 0:
        key, e = pq.remove_min()
        (x, y) = e.vertices()
        xtree = whichtree[x]
        ytree = whichtree[y]
        if xtree != ytree:
            tree.append(e)
            self._jointrees(xtree, ytree, whichtree)
    return tree


def _jointrees(self, xtree, ytree, whichtree):
    if xtree.length() < ytree.length():
        target = ytree
        deltree = xtree
    else:
        target = xtree
        deltree = ytree

    while deltree.length() > 0:
        v = deltree.pop()
        whichtree[v] = target
        target.push(v)
    del deltree
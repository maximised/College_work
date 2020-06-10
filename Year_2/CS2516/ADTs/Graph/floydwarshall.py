    def floydwarshall(self):
        """ The Floyd Warshall algorithm creates and returns a square matrix containing
            the shortest distance between every pair of vertices or infinty if there is no path
            betweeen them.
        """
        allpairs = {}
        for v in self._structure:
            allpairs[v] = {}
            for w in self._structure:
                allpairs[v][w] = float("inf")
            allpairs[v][v] = 0

        for e in self.edges():
            (v, w) = e.vertices()
            allpairs[v][w] = e.element()
            allpairs[w][v] = e.element()

        for v in self._structure:
            for w in self._structure:
                for x in self._structure:
                    if allpairs[w][x] > allpairs[w][v] + allpairs[v][x]:
                        allpairs[w][x] = allpairs[w][v] + allpairs[v][x]

        return allpairs
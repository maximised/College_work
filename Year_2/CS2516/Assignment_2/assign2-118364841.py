'''
Q1
  (i) The shortest path in a weighted graph is the path between two vertices such that
      the total sum of the weights is minimum.

  (ii) Djikstra's algorithm:
           while we still have open vertices
               pick the open vertex with lowest cost
               expand from that vertex to all neighbours not yet closed
               for each neighbour we reached
                   add the cost of the edge to the neighbour onto the cost for the
                                            vertex to get a new path cost to the neighbour
                   if the path cost is lower than the previous one, or neighbour is new
                       update the neighbours path cost
               close the current vertex

   (iii) An Adaptable Priority Queue is a Priority Queue with added compatibilities which
         allows access to all its items, not just the minimum. The keys of items are allowed to be changed,
         and items can be removed.
         You would use an APQ to store the open nodes in djikstra's algorithm.
         In the case of road maps for djikstras algorithm, the key is the cost, and the value is the
         vertex in the APQ.

'''


##################################################################
##################################################################

# Q2

def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.add_vertex(nodeid)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(graph)
    return graph


# The next classes Vertex, Edge and Graph are for the Graph ADT

class Vertex:
    """ A Vertex in a graph. """

    def __init__(self, element):
        """ Create a vertex, with a data element.

        Args:
            element - the data or label to be associated with the vertex
        """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    def __repr__(self):
        return str(self._element)

    def __lt__(self, v):
        """ Return true if this element is less than v's element.

        Args:
            v - a vertex object
        """
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element


class Edge:
    """ An edge in a graph.

        Implemented with an order, so can be used for directed or undirected
        graphs. Methods are provided for both. It is the job of the Graph class
        to handle them as directed or undirected.
    """

    def __init__(self, v, w, element):
        """ Create an edge between vertices v and w, with a data element.

        Element can be an arbitrarily complex structure.

        Args:
            element - the data or label to be associated with the edge.
        """
        self._vertices = (v, w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                + str(self._vertices[1]) + ' : '
                + str(self._element) + ')')

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered pair. """
        return self._vertices[1]

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge.

        Args:
            v - a vertex object
        """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element


class Graph:
    """ Represent a simple graph.

    This version maintains only undirected graphs, and assumes no
    self loops.
    """

    # Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the sets of edges for the corresponding vertex.
    #    Each edge set is also maintained as a dictionary,
    #    with the opposite vertex as the key and the edge object as the value.

    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()  # { vertex: {} }

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr

    # -----------------------------------------------------------------------#

    # ADT methods to query the graph

    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])  # the dict of edges for v
        return num // 2  # divide by 2, since each edege appears in the
        # vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ Return the first vertex that matches element. """
        for v in self._structure:
            if v.element() == element:
                return v
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                # to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v.

        Args:
            v - a vertex object
        """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return []

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None.

        Args:
            v - a vertex object
            w - a vertex object
        """
        if (self._structure is not None
                and v in self._structure
                and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v.

        Args:
            v - a vertex object
        """
        return len(self._structure[v])

    # ----------------------------------------------------------------------#

    # ADT methods to modify the graph

    def add_vertex(self, element):
        """ Add a new vertex with data element.

        If there is already a vertex with the same data element,
        this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

        Checks for equality between the elements. If there is special
        meaning to parts of the element (e.g. element is a tuple, with an
        'id' in cell 0), then this method may create multiple vertices with
        the same 'id' if any other parts of element are different.

        To ensure vertices are unique for individual parts of element,
        separate methods need to be written.

        """
        for v in self._structure:
            if v.element() == element:
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

        If either v or w are not vertices in the graph, does not add, and
        returns None.

        If an edge already exists between v and w, this will
        replace the previous edge.

        Args:
            v - a vertex object
            w - a vertex object
            element - a label
        """
        if v not in self._structure or w not in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements.

        Args:
            elist - a list of pairs of vertex objects
        """
        for (v, w) in elist:
            self.add_edge(v, w, None)

    # ---------------------------------------------------------------------#

    # Additional methods to explore the graph

    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv

    def depthfirstsearch(self, v):
        """ Return a DFS tree from v.

        Args:
            v - a vertex object
        """
        marked = {v: None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v, marked):
        """ Do a recursive DFS from v, storing nodes in a dictionary 'marked'.

        Args:
            v - a vertex object
            marked - a dictionary representing the DFS tree
        """
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)

    def breadthfirstsearch(self, v):
        """ Return a BFS tree from v.

        Args:
            v - a vertex object
        """
        marked = {v: None}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = e
                        nextlevel.append(x)
            level = nextlevel
        return marked

    def adaptedbreadthfirstsearch(self, v):
        """ Return a BFS tree from v with lengths from root.

        Args:
            v - a vertex object
        """
        marked = {v: 0}
        level = [v]
        level_number = 0
        while len(level) > 0:
            level_number += 1
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = level_number
                        nextlevel.append(x)
            level = nextlevel
        return marked

    def central_vertex_search(self):
        """ Return the central vertex of the graph
        """
        min_longest_path = 100000000
        for key in self.vertices():
            vlist = self.adaptedbreadthfirstsearch(key)
            max_path = max(vlist.values())
            if max_path < min_longest_path:
                min_longest_path = max_path
                central_key = key
        return str(central_key), min_longest_path, self.adaptedbreadthfirstsearch(key)


    # --------------------------------------------------- #
    # The following are special algorithms for finding specific paths and trees

    def sp(self, v, w):
        """ Gets the shortest path from v to w using the djikstras algorithm.
            v and w are vertices
        """
        if v not in self._structure or w not in self._structure:
            raise Exception("chosen nodes are not in the map")
        d = self.djikstra(v)
        path = []
        path.append((d[w][0], w))
        prev = d[w][1]
        while prev != v:
            path.append((d[prev][0], prev))
            prev = d[prev][1]

        path.append((d[prev][0], prev))

        path.reverse()

        return path

    def printvlist(self, path):
        """ prints out the path from one vertex to other calculated from sp method
        """
        print("element\tcost")
        for p in path:
            vertex = p[1]
            cost = p[0]
            element = str(vertex)
            print(element+"\t"+str(cost))

    def djikstra(self, s):
        """ Creates minimum spanning tree from vertex s

        Args:
            s - vertex from where to start the tree
        Return:
            closed - the mst dictionary {value: (key, predecessor)}
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



#################################################################################
#################################################################################

# classes Element and APQ_binary_heap are for the APQ ADT

class Element:
    """ A key, value and index. """

    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)


class APQ_binary_heap:
    ''' Adapts the Elements with keys and values into an adaptable priority queue. '''

    def __init__(self):
        self.structure = []

    def __str__(self):
        struct = self.structure
        out = {}
        for e in struct:
            out[e._key] = e
        return str(out)

    def add(self, key, item):
        """ Add an Element to the Queue and bubble it up heap to correct position.

        Args:
            key - key of the Element
            item - the Element object
        """
        l = self.length()
        e = Element(key, item, l)
        self.structure.append(e)
        self._bubble_up(l)
        return e

    def min(self):
        """ Return highest Priority Element.
        """
        return self.structure[0]._key, self.structure[0]._value

    def remove_min(self):
        """ Remove and return highest Priority Element.
        """
        # does nothing if nothing in queue
        if self.length() == 0:
            return None

        # swaps first and last element
        key, value = self.min()
        self.structure[0], self.structure[-1] = self.structure[-1], self.structure[0]
        self.structure[0]._index = 0
        self.structure.pop()
        if self.length() <= 1:
            return key, value

        # Bubble the first element down.
        self._bubble_down(0)
        return key, value

    def length(self):
        """ Return number of Elements in Queue.
        """
        return len(self.structure)

    def update_key(self, element, newkey):
        """ Assigns and updates key of element.

        Args:
            element - Elements item value (vertex)
            newkey - new key assigned to element
        """
        e = self.get_element(element)
        index = e._index
        self.structure[index]._key = newkey



        if index == 0:
            self._bubble_down(index)
        elif self.structure[index] < self.structure[(index-1)//2]:
            self._bubble_up(index)
        else:
            self._bubble_down(index)

    def update_element(self, value, new_value):
        """ Change value of element with value to new_value

        Args:
            value - current value of Element
            new_value - new value we will assign to Element
        """
        e = self.get_element(value)
        e._value = new_value


    def get_key(self, value):
        """ Return key of element with value

        Args:
            value - Element._value
        """
        e = self.get_element(value)
        return e._key

    def remove(self, element):
        """ Remove and return element of Queue.

        Args:
            element - Element object
        """
        # does nothing if nothing in queue
        if self.length() == 0:
            return None

        e = self.get_element(element)
        index = e._index

        self.structure[index], self.structure[-1] = self.structure[-1], self.structure[index]
        self.structure[index]._index = index
        self.structure.pop()

        # if last element is removed
        if index >= self.length():
            return e._key, e._value

        # if any other element is removed, bubble swapped element
        if index == 0:
            self._bubble_down(index)
        elif self.structure[index] < self.structure[(index-1)//2]:
            self._bubble_up(index)
        else:
            self._bubble_down(index)
        return e._key, e._value

    def _bubble_up(self, l):
        """ Bubbles an element up the queue to its position based on key

        Args:
            i - index of element to be bubbled up
        """
        while self.structure[l]< self.structure[(l-1)//2] and l > 0: # bubbles e up the queue
            self.structure[l], self.structure[(l - 1) // 2] = self.structure[(l - 1) // 2], self.structure[l]
            self.structure[l]._index = l
            self.structure[(l - 1) // 2]._index = (l-1)//2
            l = (l-1)//2

    def _bubble_down(self, i):
        """ Bubbles an element down the queue to its position based on key

        Args:
            i - index of element to be bubbled down
        """
        while i*2+1 < self.length():
            if i*2+2 >= self.length():
                j = i*2+1
            elif self.structure[i * 2 + 1] < self.structure[i * 2 + 2]:
                j = i * 2 + 1
            else:
                j = i * 2 + 2
            if self.structure[i] > self.structure[j]:
                self.structure[i], self.structure[j] = self.structure[j], self.structure[i]
                self.structure[i]._index = i
                self.structure[j]._index = j
                i = j
            else:
                break

    def get_element(self, value):
        """ finds element object based on its item value

        Args:
            value - item value of object being searched
        """
        for e in self.structure:
            if value == e._value:
                return e
        return None



# ------------------------------------------------- #
# Testing code below

print("simplegraph1:")
graph = graphreader("simplegraph1.txt")
print(graph)
print()

print("djikstra's test between vertices 1 and 4:")
source = graph.get_vertex_by_label(1)
dest = graph.get_vertex_by_label(4)
route = graph.sp(source, dest)
graph.printvlist(route)
print()
print("djikstra's test from v1 to all vertices (vertex: (cost to it, predecessor)):")
djikstra = graph.djikstra(source)
print(djikstra)
print()
print()


print("simplegraph2:")
graph = graphreader("simplegraph2.txt")
print(graph)
print()

print("simplegraph2:\ndjikstra's test between vertices 14 and 5:")
source = graph.get_vertex_by_label(14)
dest = graph.get_vertex_by_label(5)
route = graph.sp(source, dest)
graph.printvlist(route)
print()
print("djikstra's test from v14 to all vertices (vertex: (cost to it, predecessor)):")
djikstra = graph.djikstra(source)
print(djikstra)

print(graph)
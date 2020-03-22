from functools import total_ordering


@total_ordering
class Movie:
    """ Represents a single Movie. """

    def __init__(self, i_title, i_date, i_runtime):
        """ Initialise a Movie Object. """
        self._title = i_title
        self._date = i_date
        self._time = i_runtime

    def __str__(self):
        """ Return a short string representation of this movie. """
        outstr = self._title
        return outstr

    def full_str(self):
        """ Return a full string representation of this movie. """
        outstr = self._title + ": "
        outstr = outstr + str(self._date) + "; "
        outstr = outstr + str(self._time)
        return outstr

    def get_title(self):
        """ Return the title of this movie. """
        return self._title

    def __eq__(self, other):
        """ Return True if this movie has exactly same title as other. """
        if (other._title == self._title):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this movie has exactly same title as other. """
        return not (self._title == other._title)

    def __lt__(self, other):
        """ Return True if this movie is ordered before other.

        A movie is less than another if it's title is alphabetically before.
        """
        if other._title > self._title:
            return True
        return False


class BSTNode:
    """ An internal node for a Binary Search Tree.

    This is a general BST, but with a small number of additional methods to
    implement a movie library. The title of the Movie is used as the search
    key.
    """

    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        if self._element:
            outstr = ''
            if self._rightchild or self._leftchild:
                if self._leftchild:
                    outstr += self._leftchild.__str__() + '/'
                outstr += self._element.__str__() + '/'
                if self._rightchild:
                    outstr += self._rightchild.__str__() + '/'
                return outstr
            else:
                return self._element.__str__() + '/'
        else:
            return ''

        # method body goes here

    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
                + '; height = ' + str(self.height()))

    def search(self, title):
        cur_title = self._element._title

        if title < cur_title:
            if self._leftchild is None:
                return None
            else:
                self._leftchild.search(title)
        elif cur_title < title:
            if self._rightchild is None:
                return None
            else:
                self._rightchild.search(title)
        else:
            return self._element
        """ Return the Movie object with that movie title, or None.

        This method is specific to the Movie library.
        """
        # method body goes here

    def search_node(self, searchitem):
        """ Return the node (with subtree) containing searchitem, or None. """
        # method body goes here

    def add(self, obj):
        if obj < self._element:
            if self._leftchild is None:
                self._leftchild = BSTNode(obj)
                self._leftchild._parent = self
            else:
                self._leftchild.add(obj)
        elif self._element < obj:
            if self._rightchild is None:
                self._rightchild = BSTNode(obj)
                self._rightchild._parent = self
            else:
                self._rightchild.add(obj)
        else:
            return
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        # method body goes here

    def findmaxnode(self):
        """ Return the BSTNode with the maximal element at or below here. """
        if self._rightchild:
            self._rightchild.findmaxnode()
        else:
            return self


    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        if self is None:
            return 0
        elif self._leftchild is None and self._rightchild is None:
            return 1
        elif self._leftchild and self._rightchild is None:
            return 1 + self._leftchild.height()
        elif self._rightchild and self._leftchild is None:
            return 1 + self._rightchild.height()
        else:
            return 1 + max(self._leftchild.height, self._rightchild.height())


    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree.
        """
        if self is None:
            return 0
        elif self._leftchild is None and self._rightchild is None:
            return 1
        elif self._leftchild and self._rightchild is None:
            return 1 + self._leftchild.size()
        elif self._rightchild and self._leftchild is None:
            return 1 + self._rightchild.size()
        else:
            return 1 + self._leftchild.size() + self._rightchild.size()


    def leaf(self):
        """ Return True if this node has no children. """
        if self._leftchild is None and self._rightchild is None:
            return True
        else:
            return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        count = 0
        if self._leftchild:
            count += 1
        if self._rightchild:
            count += 1

        if count == 1:
            return True
        else:
            return False

    def full(self):
        """ Return true if this node has two children. """
        if self._leftchild and self._rightchild:
            return True
        else:
            return False

    def internal(self):
        """ Return True if this node has at least one child. """
        if not (self._leftchild is None and self._rightchild is None):
            return True
        else:
            return False

    def remove(self, title):
        """ Remove and return a movie.

        This method is specific to the Movie library.
        Remove the movie with the given title from the tree rooted at this node.
        Maintains the BST properties.
        """
        # method body goes here

    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        removed = self

        if self.full():
            new_max = self._leftchild.findmaxnode()
            old_max = self._leftchild.findmaxnode()
            if self._parent:
                new_max._parent = self._parent
            new_max._leftchild = self._leftchild
            new_max._rightchild = self._rightchild
            self = new_max

            old_max._parent._rightchild = None
            if old_max._leftchild:
                old_max._leftchild._parent = old_max._parent
                old_max._parent._rightchild = old_max._leftchild
            old_max._parent = None
            return old_max._element

        elif self.leaf():
            parent = self._parent
            if self == parent._leftchild:
                parent._leftchild = None
            else:
                parent._rightchild = None

            self._parent
            self = removed._parent
            return removed._element
        elif self._leftchild and not self._rightchild:
            self._leftchild._parent = self._parent
            new_node = self._leftchild
            self._leftchild = None
            self.__dict__.update(new_node.__dict__)
            print(removed._element)

            return removed._element
        elif self._rightchild and not self._leftchild:
            if self._parent:
                self._rightchild._parent = self._parent
                self._parent._rightchild = self._rightchild
                self._parent = None
            self._rightchild = None
            self = removed._leftchild

            return removed._element



        # if this is a full node
        # find the biggest item in the left tree
        #  - there must be a left tree, since this is a full node
        #  - the node for that item can have no right children
        # move that item up into this item
        # remove that old node, which is now a semileaf
        # return the original element
        # else if this has no children
        # find who the parent was
        # set the parent's appropriate child to None
        # wipe this node
        # return this node's element
        # else if this has no right child (but must have a left child)
        # shift leftchild up into its place, and clean up
        # return the original element
        # else this has no left child (but must have a right child)
        # shift rightchild up into its place, and clean up
        # return the original element

        # method body goes here

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if self._isthisapropertree() == False:
            print("ERROR: this is not a proper tree. +++++++++++++++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self._leftchild._element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._leftchild is not None:
            self._leftchild._print_structure()
        if self._rightchild is not None:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild is not None:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild is not None:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False
        if self._parent is not None:
            if (self._parent._leftchild != self
                    and self._parent._rightchild != self):
                ok = False
        return ok

    def _testadd():
        node = BSTNode(Movie("Memento", "11/10/2000", 113))
        node._print_structure()
        print('> adding Melvin and Howard')
        node.add(Movie("Melvin and Howard", "19/09/1980", 95))
        node._print_structure()
        print('> adding a second version of Melvin and Howard')
        node.add(Movie("Melvin and Howard", "21/03/2007", 112))
        node._print_structure()
        print('> adding Mellow Mud')
        node.add(Movie("Mellow Mud", "21/09/2016", 92))
        node._print_structure()
        print('> adding Melody')
        node.add(Movie("Melody", "21/03/2007", 113))
        node._print_structure()
        print(node.findmaxnode()._element)
        print(node.findmaxnode()._element)
        node._print_structure()
        print("removing")
        node.remove_node()
        node._print_structure()
        print(node._element)
        return node

    def _test():
        node = BSTNode(Movie("B", "b", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "A")
        node.add(Movie("A", "a", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "A")
        node.remove("A")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "F")
        node.add(Movie("F", "f", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "D")
        node.add(Movie("D", "d", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "E")
        node.add(Movie("E", "e", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "D")
        node.remove("D")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "E")
        node.remove("E")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "L")
        node.add(Movie("L", "l", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "H")
        node.add(Movie("H", "h", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "I")
        node.add(Movie("I", "i", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "G")
        node.add(Movie("G", "g", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "L")
        node.remove("L")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "H")
        node.remove("H")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "I")
        node.remove("I")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "G")
        node.remove("G")
        print('Ordered:', node)
        node._print_structure()
        print(node)


def build_tree(filename):
    """ Return a BST tree of Movie files built from filename. """

    # open the file
    file = open(filename, 'r')

    # Create the root node  of a BST with a Movie object created from the
    # first line in the file
    inputlist = file.readline().split('\t')
    for item in inputlist:
        print(item)
    movie = Movie(inputlist[0], inputlist[1], inputlist[2])
    bst = BSTNode(movie)
    count = 1

    # now cycle through the other lines in the file, creating the Movie
    # objects and adding them to the BST
    for line in file:
        inputlist = line.split('\t')
        movie = Movie(inputlist[0], inputlist[1], inputlist[2])
        added = bst.add(movie)
        if added != None:
            count += 1

    # print out some info for sanity checking
    print("Built a tree of height " + str(bst.height()))
    print("with", count, "movies")
    return bst

BSTNode._testadd()
# print('++++++++++')
# BSTNode._test()


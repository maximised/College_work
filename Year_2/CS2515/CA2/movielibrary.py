'''
Q2
smallmovies.txt:
unique movies = 12
height = 4
minimum height = 3

"Four Lions":
statistics -> size = 2; height = 1
ordered_sequence =
Four Lions
Four Lovers

"Wonder Woman"
Not in the Binary Tree

"Touch of Evil"
Not in the Binary Tree

"Delicatessen"
Not in the Binary Tree
#########################################################################################################

small_repeated_movies.txt:
unique movies = 19
height = 7
minimum height = 4

"Four Lions":
Not in the Binary Tree

"Wonder Woman"
statistics -> size = 1; height = 0
ordered_sequence =
Wonder Woman

"Touch of Evil"
Not in the Binary Tree

"Delicatessen"
Not in the Binarry Tree

###################################################################################################

movies.txt:
unique movies = 41750
height = 34
minimum height = 15

"Four Lions":
statistics -> size = 2; height = 1
ordered_sequence =
Four Lions
Four Lovers

"Wonder Woman"
statistics -> size = 1; height = 0
ordered_sequence =
Wonder Woman

"Touch of Evil"
statistics -> size = 10; height = 5
ordered_sequence =
Touch
Touch and Go
Touch of Death
Touch of Evil
Touch of Pink
Touch of the Light
Touch the Sound
Touch the Top of the World
Touchback
Touched with Fire

"Delicatessen"
statistics -> size = 11; height = 7
ordered_sequence =
Delbaran
Delgo
Delhi Belly
Delhi Dance
Delhi Safari
Delhi in a Day
Delhi-6
Deli Man
Delicacy
Delicatessen
Delirious

'''





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

#Q1
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
            outstr = ''                         # we use recursion to add movie titles
            if self.internal():
                if self._leftchild:
                    outstr += self._leftchild.__str__()

                outstr += '\n'
                outstr += self._element.__str__()

                if self._rightchild:
                    outstr += self._rightchild.__str__()

                return outstr
            else:
                return '\n' + self._element.__str__()
        else:
            return ''


    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
                + '; height = ' + str(self.height()))

    def search(self, title):
        """ Return the Movie object with that movie title, or None.

        This method is specific to the Movie library.
        """
        cur_title = self._element._title

        # recursively search the sub tree the movie is in

        if title < cur_title:
            if self._leftchild is None:
                return None
            else:
                return self._leftchild.search(title)
        elif cur_title < title:
            if self._rightchild is None:
                return None
            else:
                return self._rightchild.search(title)
        else:
            return self._element


    def search_node(self, searchitem):
        """ Return the node (with subtree) containing searchitem, or None. """
        if searchitem is None:
            return None

        cur_item = self._element

        # recursively search the sub tree with the movie

        if searchitem < cur_item:
            if self._leftchild is None:
                return None
            else:
                return self._leftchild.search_node(searchitem)
        elif cur_item < searchitem:
            if self._rightchild is None:
                return None
            else:
                return self._rightchild.search_node(searchitem)
        else:
            return self

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        if self._element is None:  # if out tree is empty, make root node the added obj
            self._element = obj
            return self


        # recursively search sub tree
        if obj < self._element:
            if self._leftchild is None:
                self._leftchild = BSTNode(obj)
                self._leftchild._parent = self
                return self._leftchild
            else:
                return self._leftchild.add(obj)
        elif self._element < obj:
            if self._rightchild is None:
                self._rightchild = BSTNode(obj)
                self._rightchild._parent = self
                return self._rightchild
            else:
                return self._rightchild.add(obj)
        else:
            return None


    def findmaxnode(self):
        """ Return the BSTNode with the maximal element at or below here. """
        if self._rightchild:
            return self._rightchild.findmaxnode()
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
            return 0
        elif self._leftchild and self._rightchild is None:
            return 1 + self._leftchild.height()
        elif self._rightchild and self._leftchild is None:
            return 1 + self._rightchild.height()
        else:
            return 1 + max(self._leftchild.height(), self._rightchild.height())


    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree.
        """
        if self._element is None:
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
        if self._element is None:
            return None

        node_to_remove = self.search_node(self.search(title))
        if node_to_remove is not None:
            node_to_remove.remove_node()

    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
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


        # if our tree is empty, do nothing
        if self is None:
            return None

        removed_element = self._element

        # recursive
        if self.full():
            biggest = self._leftchild.findmaxnode()
            self._element = biggest._element

            if biggest._parent != self:
                biggest._parent._rightchild = None

            if biggest._leftchild:
                biggest._leftchild._parent = biggest._parent
            biggest._parent._leftchild = biggest._leftchild
            biggest._parent = None
            biggest._element = None
            del biggest

            return removed_element


        elif self.leaf():
            if self._parent:
                if self._parent._leftchild == self:
                    self._parent._leftchild = None
                else:
                    self._parent._rightchild = None

            self._parent = None

            self._element = None

            return removed_element

        elif self._leftchild and not self._rightchild:
            self._element = self._leftchild._element
            self._leftchild, self._rightchild = self._leftchild._leftchild, self._leftchild._rightchild

            if self._leftchild:
                self._leftchild._parent = self
            if self._rightchild:
                self._rightchild._parent = self

            return removed_element


        elif self._rightchild and not self._leftchild:
            self._element = self._rightchild._element
            self._leftchild, self._rightchild = self._rightchild._leftchild, self._rightchild._rightchild

            if self._rightchild:
                self._rightchild._parent = self
            if self._leftchild:
                self._leftchild._parent = self

            return removed_element


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
        node.add(Movie("Velocity", "20/02/2015", 110))
        node._print_structure()
        print(node.search("Melvin and Howard"))
        node._print_structure()

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
        if added is not None:
            count += 1

    # print out some info for sanity checking
    print("Built a tree of height " + str(bst.height()))
    print("with", count, "movies")
    return bst

#BSTNode._testadd()
#print('++++++++++')
#BSTNode._test()


##########################################################

#Q2

filename1 = "/users/bscdsa2022/mc64/Downloads/smallmovies.txt"
filename2 = "/users/bscdsa2022/mc64/Downloads/small_repeated_movies.txt"
filename3 = "/users/bscdsa2022/mc64/Downloads/movies.txt"

#bst1 = build_tree(filename1)
#print(bst1.search_node(bst1.search("Four Lions"))._stats())
#print(bst1.search_node(bst1.search("Four Lions")))
#print(bst1.search_node(bst1.search("Wonder Woman"))._stats())
#print(bst1.search_node(bst1.search("Wonder Woman")))
#print(bst1.search_node(bst1.search("Touch of Evil"))._stats())
#print(bst1.search_node(bst1.search("Touch of Evil")))
#print(bst1.search_node(bst1.search("Delicatessen"))._stats())
#print(bst1.search_node(bst1.search("Delicatessen")))


#bst2 = build_tree(filename2)
#print(bst2.search_node(bst2.search("Four Lions"))._stats())
#print(bst2.search_node(bst2.search("Four Lions")))
#print(bst2.search_node(bst2.search("Wonder Woman"))._stats())
#print(bst2.search_node(bst2.search("Wonder Woman")))
#print(bst2.search_node(bst2.search("Touch of Evil"))._stats())
#print(bst2.search_node(bst2.search("Touch of Evil")))
#print(bst2.search_node(bst2.search("Delicatessen"))._stats())
#print(bst2.search_node(bst2.search("Delicatessen")))


#bst3 = build_tree(filename3)
#print(bst3.search_node(bst3.search("Four Lions"))._stats())
#print(bst3.search_node(bst3.search("Four Lions")))
#print(bst3.search_node(bst3.search("Wonder Woman"))._stats())
#print(bst3.search_node(bst3.search("Wonder Woman")))
#print(bst3.search_node(bst3.search("Touch of Evil"))._stats())
#print(bst3.search_node(bst3.search("Touch of Evil")))
#print(bst3.search_node(bst3.search("Delicatessen"))._stats())
#print(bst3.search_node(bst3.search("Delicatessen")))

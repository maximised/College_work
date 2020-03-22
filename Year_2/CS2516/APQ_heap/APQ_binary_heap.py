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


class APQ_binary_heap:
    ''' Adapts the Elements with keys into an adaptable priority queue. '''

    def __init__(self):
        self.structure = list()

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
        return self.structure[0]

    def remove_min(self):
        """ Remove and return highest Priority Element.
        """
        # does nothing if nothing in queue
        if self.length() == 0:
            return None

        # swaps first and last element
        e = self.min()
        self.structure[0], self.structure[self.length()-1] = self.structure[self.length()-1], self.structure[0]
        self.structure.pop()
        if self.length() <= 1:
            return e

        # Bubble the first element down.
        self._bubble_down(0)
        return e

    def length(self):
        """ Return number of Elements in Queue.
        """
        return len(self.structure)

    def update_key(self, element, newkey):
        """ Assigns and updates key of element.

        Args:
            element - Element object
            newkey - new key assigned to element
        """
        index = element._index
        self.structure[index]._key = newkey

        if index == 0:
            self._bubble_down(index)
        elif self.structure[index] < self.structure[(index-1)//2]:
            self._bubble_up(index)
        else:
            self._bubble_down(index)

    def get_key(self, element):
        """ Return key of element

        Args:
            element - Element object
        """
        index = element._index
        return self.structure[index]._key

    def remove(self, element):
        """ Remove and return element of Queue.

        Args:
            element - Element object
        """
        # does nothing if nothing in queue
        if self.length() == 0:
            return None

        index = element._index
        e = self.structure[index]

        self.structure[index], self.structure[self.length()-1] = self.structure[self.length()-1], self.structure[index]
        self.structure.pop()

        # if last element is removed
        if index >= self.length():
            return e

        # if any other element is removed, bubble swapped element
        if index == 0:
            self._bubble_down(index)
        elif self.structure[index] < self.structure[(index-1)//2]:
            self._bubble_up(index)
        else:
            self._bubble_down(index)
        return e

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


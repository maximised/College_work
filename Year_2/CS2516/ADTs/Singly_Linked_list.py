class SLLNode:
    def __init__(self, item, nextnode):
        self.element = item
        self.next = nextnode

class SLinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def length(self):
        return self.size

    def add_first(self, item):
        newnode = SLLNode(item, self.first)
        self.first = newnode
        self.size = self.size + 1

    def get_first(self):
        if self.size == 0:
            return None
        return self.first.element

    def remove_first(self):
        if self.size == 0:
            return None
        item = self.first.element
        self.first = self.first.next
        self.size = self.size - 1
        return item

    def add_last(self, item):
        newnode = SLLNode(item, None)
        if self.first == None:
            self.first = newnode
        else:
            node = self.first
            while node.next:
                node = node.next
            node.next = newnode
        self.size = self.size + 1

    def get_last(self):
        if self.size == 0:
            return None

        node = self.first
        while node.next:
            node = node.next
        return node.element


##################################################################
# Test code

def test_linkedlist():
    mylist = SLinkedList()
    mylist.add_first('b')
    mylist.add_last('c')
    mylist.add_first('a')
    mylist.add_last('d')
    mylist.add_last('e')
    print('mylist =', mylist)
    print('length =', mylist.length())
    print('first =', mylist.get_first())
    print('last = ', mylist.get_last())
    print('first (removed) =', mylist.remove_first())
    print('mylist now =', mylist)
    print('length =', mylist.length())
    mylist.remove_first()
    mylist.remove_first()
    mylist.remove_first()
    mylist.remove_first()
    print('length =', mylist.length())
    print('first (None?) =', mylist.get_first())
    print('last (None?) =', mylist.get_last())
    print('first removed (None?) =', mylist.remove_first())
    mylist.add_last('f')
    print('mylist (f) =', mylist)
    print('length =', mylist.length())

test_linkedlist()
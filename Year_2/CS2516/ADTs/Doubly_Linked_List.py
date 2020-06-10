class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode

class DLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add_after(self, item, before):
        node = DLLNode(item, before, before.next)
        before.next = node
        if node.next is not None:
            node.next.prev = node
        self.size += 1

    def add_first(self, item):
        node = DLLNode(item, None, self.first)
        self.first = node
        if self.size == 0:  # add same two lines to remove_first(...)
            self.last = node
        self.size = self.size + 1

    def add_last(self, item):
        newnode = DLLNode(element, self.last, None)
        if self.first == None:
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode
        self.last = newnode
        self.size = self.size + 1

    def get_first(self):
        if self.size == 0:
            return None
        return self.first.element

    def get_last(self):
        if self.size == 0:
            return None
        return self.last.element

    def remove_node(self, node):
        if self.size == 0:
            return None
        temp = node
        node.next.prev = node.prev
        node.prev.next = node.next

    def remove_first(self):
        if self.size == 0:
            return None
        self.first = self.first.next
        if self.size == 1:
            self.last = None
        else:
            self.first.prev = None
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None
        self.last = self.last.prev
        if self.size == 1:
            self.first = None
        else:
            self.last.next = None
        self.size -= 1
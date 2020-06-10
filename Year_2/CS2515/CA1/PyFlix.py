class Movie:
    def __init__(self, title, director, cast, length):
        self.title = title
        self.director = director
        self.cast = cast
        self.length = length
        self.rating = -1

    def __str__(self):
        return "title: {}, director: {}".format(self.title, self.director)

    def get_info(self):
        return "title: {}\ndirector: {}\ncast: {}\nlength: {}\nrating: {}".format(self.title,
                                                                                       self.director,
                                                                                       self.cast,
                                                                                       self.length,
                                                                                       self.rating)


import re


class DLLNode:
    def __init__(self, item, prev=None, next=None):
        self.element = item
        self.prev = prev
        self.next = next


class PyFlix:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        self.selected_node = None

    def __str__(self):
        # if self.length == 0:
        #    return None

        s = "$$$ Pyflix Library:\n"
        '''
        node = self.first
        while node.next:
            if node == self.selected_node:
                s += '-->'
            s += "(title: {}, director: {})\n".format(node.element.title, node.element.director)
            node = node.next
        if node == self.selected_node:
            s += '-->'
        s += "(title: {}, director: {})\n".format(node.element.title, node.element.director)
        s += "$$$"
        '''
        node = self.first
        while node:
            if node == self.selected_node:
                s += '-->'
            s += "(title: {}, director: {})\n".format(node.element.title, node.element.director)
            node = node.next
        s += '$$$\n'

        return s

    def add_movie(self, movie):
        newnode = DLLNode(movie, prev=self.last)

        if self.length == 0:
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode

        self.length += 1

    def get_current(self):
        if self.selected_node:
            return "Current movie: {}, {}\n".format(self.selected_node.element.title,
                                                    self.selected_node.element.director)

    def next_movie(self):
        if self.selected_node == None:
            self.selected_node = self.first
        else:
            self.selected_node = self.selected_node.next

    def prev_movie(self):
        self.selected_node = self.selected_node.prev

    def reset(self):
        if self.selected_node == None:
            self.selected_node = self.last
        else:
            self.selected_node = self.selected_node.next

    def rate(self):
        if self.selected_node == None:
            print("No movie is selected.")
            return None
        r = str(input("{}Enter your rating [0 to 4]: ".format(self.get_current())))

        self.selected_node.element.rating = r
        print("Your rating was {}\n".format(r))

    def info(self):
        if self.selected_node == None:
            return None

        return self.selected_node.element.get_info()

    def remove_current(self):
        if self.selected_node == None:
            return None
        elif self.selected_node == self.last:
            self.selected_node.prev.next = None
            self.selected_node.prev = self.last
        elif self.selected_node == self.first:
            self.selected_node.next.prev = None
            self.first = self.selected_node.next
        else:
            self.selected_node.prev.next = self.selected_node.next
            self.selected_node.next.prev = self.selected_node.prev

        self.length -= 1

        removed_node = self.selected_node
        if self.selected_node.next:
            self.selected_node = self.selected_node.next
        else:
            if self.first:
                self.selected_node = self.first
        return removed_node.element.get_info()


    def length(self):
        return self.length

    ###################################################

    def search(self, word):
        word = word.lower()

        node = self.selected_node

        if node.next == None:
            node = self.first
        else:
            node = node.next

        while node != self.selected_node:
            l = (node.element.get_info()).split('\n')
            node_content = [i[i.find(': ') + 2:].lower() for i in l]
            # v = vars(node.element)
            # node_content = list([str(i).lower() for i in v.values()])

            if any([re.search(word, i) for i in node_content]):
                self.selected_node = node
                print(node.element.get_info())
                return
            if node.next == None:
                node = self.first
            else:
                node = node.next

        l = (node.element.get_info()).split('\n')
        node_content = [i[i.find(': ') + 2:].lower() for i in l]

        if any([re.search(word, i) for i in node_content]):
            self.selected_node = node
            print(node.element.get_info())
            return

        print('no matching movie\n')



def test():
    pyflix_list = PyFlix()

    m1 = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)
    pyflix_list.add_movie(m1)

    m2 = Movie("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
    pyflix_list.add_movie(m2)

    m3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)
    pyflix_list.add_movie(m3)

    print(pyflix_list)

    pyflix_list.next_movie()

    print(pyflix_list.info())

    pyflix_list.next_movie()

    print(pyflix_list.get_current())

    pyflix_list.rate()

    pyflix_list.prev_movie()

    print(pyflix_list)

    pyflix_list.remove_current()

    print(pyflix_list)

    print(pyflix_list.get_current())

    m4 = Movie("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)
    pyflix_list.add_movie(m4)

    pyflix_list.next_movie()

    pyflix_list.next_movie()

    pyflix_list.get_current()

    print(pyflix_list)

    pyflix_list.search('joker')

    print(pyflix_list)

    pyflix_list.search('fundon')

    print(pyflix_list)

test()
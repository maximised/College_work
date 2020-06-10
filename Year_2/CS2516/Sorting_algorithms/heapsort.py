def heapsort(inlist):
    """ Heapsort (the list) inlist, in place.

        Worst case time complexity: O(n*logn)
    """

    # first treat the inlist as the input stream to build a *max* priority queue
    # maintain the PQ in the same list, gradually growing from the front.
    # that means each item to be added will already be in the starting point
    # and so all we have to do is bubble each item up the heap which is earlier
    # than it in the list.
    # Once the PQ is complete, we need to reverse it.
    # Gradually shrink the PQ by removing the *max* item, and place it in the
    # cell at the end of the PQ just vacated

    length = len(inlist)
    print(inlist, ': initial list')
    for i in range(length):
        print('   add', inlist[i], 'to the virtual heap')
        bubbleup(inlist,i)
        print(inlist)
    for i in range(length):
        # elt to be moved up is in position len(list)-1 - i
        # max elt being shifted is in position 0, and is going to len(list)-1-i
        # so start by swapping them, and then bubbling down the new elt in pos 0
        # remembering that hea hap size has shrunk by 1.

        print('shifting', inlist[0], 'to cell', (length-1-i))
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist, 0, length-2-i)
        print(inlist)

def bubbleup(inlist, i):
    """ Bubble up item currently in pos i in a max heap. """
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            print('swapping:', inlist[i], 'with its parent:', inlist[parent])
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0


def bubbledown(inlist, i, last):
    """ Bubble down item currently in pos i in a max heap (stops at last). """
    while last > (i*2):  # so at least one child
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc   # start by assuming left child is the max child
        if last > lc and inlist[rc] > inlist[lc]:  #r c exists and is bigger
            maxc = rc
        if inlist[i] < inlist[maxc]:
            print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last



################################################
# test code

l = [8,15,3,23,7,19,25,4,12,18]

heapsort(l)

print()

print(l)
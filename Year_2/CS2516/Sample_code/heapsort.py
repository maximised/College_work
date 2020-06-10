
""" Heapsort and randomised testing

    Solutions to Lab 01, CS2516, 2020
"""

import random #for generating random lists for tests, and for quicksort
import copy #to generate copies, so that we don't sort a previously sorted list
import time #for evaluating the runtime of the methods

def insertionsort(mylist):
    """ Sort (the list) myList in place, using Insertion sort.

    Note - improved version compared to the lecture slides, cutting
    out one repeated internal loop.
    """
    n = len(mylist)
    i=1
    # print(mylist, ': start by leaving', mylist[0], 'in place')
    while i < n:
        temp = mylist[i]
        j = i-1
        while temp < mylist[j] and j > -1:
            mylist[j+1] = mylist[j]
            j -= 1
        mylist[j+1] = temp
        # print(mylist, ': after inserting', temp)
        i += 1

# simple test
# insertionsort([5,3,7,4,2,6])



def heapsort(inlist):
    """ Heapsort (the list) inlist, in place. """

    # first treat the inlist as the input stream to build a *max* priority queue
    # maintain the PQ in the same list, gradually growing from the front.
    # that means each item to be added will already be in the starting point
    # and so all we have to do is bubble each item up the heap which is earlier
    # than it in the list.
    # Once the PQ is complete, we need to reverse it.
    # Gradually shrink the PQ by removing the *max* item, and place it in the
    # cell at the end of the PQ just vacated

    length = len(inlist)
    # print(inlist, ': initial list')
    for i in range(length):
        # print('   add', inlist[i], 'to the virtual heap')
        bubbleup(inlist,i)
        # print(inlist)
    for i in range(length):
        # elt to be moved up is in position len(list)-1 - i
        # max elt being shifted is in position 0, and is going to len(list)-1-i
        # so start by swapping them, and then bubbling down the new elt in pos 0
        # remembering that hea hap size has shrunk by 1.

        # print('shifting', inlist[0], 'to cell', (length-1-i))
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist, 0, length-2-i)
        # print(inlist)


def bubbleup(inlist, i):
    """ Bubble up item currently in pos i in a max heap. """
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            #print('swapping:', inlist[i], 'with its parent:', inlist[parent])
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
            #print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last

# simple test
# heapsort([5,3,7,4,2,6])


def test(func, inlist):
    """ Test sorting algorithm func on (list) inlist. """
    start_time = time.perf_counter()
    func(inlist)
    end_time = time.perf_counter()
    res = sortingerrorcheck(inlist, func)
    if res == -1:
        return res
    return (end_time - start_time)

def testrandom(flist, n):
    """ each sort algorithm func on a randomised list of the first n ints. """
    times = []
    testlist = [i for i in range(n)]
    random.shuffle(testlist)
    # print(testlist, ': the randomised input list of length', n)
    for func in flist:
        copylist = copy.copy(testlist)
        # print('Algorithm', func.__name__, 'is being asked to sort', copylist)
        times.append(test(func, copylist))
    return times

def testaverage(flist, n, number):
    """ Evaluate each algorithm in flist on a set of randomised lists.

        n is the size of the list (which contains the first n integers).
        number is the number of lists in the set.
        The function returns the mean runtime for each algorithm.
    """
    averages = [0] * len(flist)

    j = 0
    while j < number:
        times = testrandom(flist,n)
        for i in range(len(flist)):
            averages[i] += times[i]
        j += 1

    for i in range(len(flist)):
        averages[i] = averages[i] / number
    return averages

def sortingerrorcheck(testlist, f):
    """ Check that (list) testist is actually sorted. f is the algorithm used.

    Returns 0 if it is sorted correctly; -1 otherwise (and prints a message)
    """
    errors = False
    firsterror = -1
    i = 0
    end  = len(testlist)-1
    while i < end and errors == False:
        if testlist[i] > testlist[i+1]:
            errors = True
            firsterror = i
        i += 1
    if errors:
        print('    ERROR: first position:', firsterror, 'with value',
              testlist[firsterror],
              'followed by', testlist[firsterror+1])
        print('using algorith:', f.__name__)
        print(testlist)
        return -1
    else:
        return 0

"""
testlist = [5,3,7,4,2,6]
print(testlist, ': initial list')
test(heapsort, testlist)
print(testlist, ': final list')
"""

"""
flist = [heapsort, insertionsort]
times = testrandom(flist,10000)
i = 0
while i < len(flist):
    print(flist[i].__name__, ':', times[i])
    i += 1
"""

flist = [heapsort, insertionsort]
listsize = 1000
number = 20
print('Testing algorithms on', number, 'random lists of length', listsize)
print('Average time per algorithm per list:')
averages = testaverage(flist, listsize, number)
i = 0
while i < len(flist):
    print(flist[i].__name__, ':', averages[i])
    i += 1
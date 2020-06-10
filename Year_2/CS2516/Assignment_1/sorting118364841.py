'''
Generally for the evaluateall function, the algorithms ranks from slowest to fastest: heapsort, mergesort, quicksort, python.
The runtimes increase as the size of lists increase. python is by far the fastest and quicksort is faster then mergesort most of the time.
for the evaluatepartial function, the algorithms ranks from slowest to fastest: mergesort, heapsort, quicksort, python.
'''


# Q1
'''
(i) mergesort worst case complexity is O(nlogn) while quicksort is O(n^2). However, quicksort is faster most of the time.
    mergesort sorts by dividing, sorting the slices and combining. quicksort also does this but the combination phase is faster.

(ii) time complexity is: O(nlogn)

(iii) standard mergesort: O(n)
      bottom up mergesort: O(n)
'''

##############################################################################

# Q2

def quicksort(mylist):
    n = len(mylist)
    for i in range(len(mylist)):
        j = random.randint(0, n-1)
        mylist[i], mylist[j] = mylist[j], mylist[i]
    _quicksort(mylist, 0, n-1)

def  _quicksort(list, pivot, end):
    if pivot < end:
        right_index = end
        left_index = pivot
        sub_pivot = pivot
        pivot_value = list[pivot]
        while (left_index <= right_index):
            while left_index <= right_index:
                if (pivot_value > list[right_index]):
                    sub_pivot = right_index
                    break
                right_index -= 1

            while (left_index < right_index) and (list[left_index] <= pivot_value):
                left_index += 1

            if (left_index <= right_index):
                list[right_index], list[left_index] = list[left_index], list[right_index]
                sub_pivot = left_index
                right_index -= 1
                left_index += 1
        list[sub_pivot], list[pivot] = list[pivot], list[sub_pivot]
        _quicksort(list, pivot, sub_pivot-1)
        _quicksort(list, sub_pivot+1, end)


##############################################################################

# Q3

# mergesort
def merge(list1, list2, mylist):
    f1 = 0
    f2 = 0
    while f1+f2 < len(mylist):
        if f1 == len(list1):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            mylist[f1+f2] = list2[f2]
            f2 += 1
        else:
            mylist[f1+f2] = list1[f1]
            f1 += 1


def mergesort(mylist):
    n = len(mylist)
    if n > 1:
        list1 = mylist[:n//2]
        list2 = mylist[n//2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)


# heapsort

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

######################################################################################################

# Q4
import copy
import random
from time import perf_counter

def evaluateall(n, k):
    random_list = random.sample(range(0, 1000000), n-k)
    for i in range(k):
        random_list.append(random.choice(random_list[0: n-k-1]))

    list_of_lists = []
    for i in range(10):
        list_of_lists.append(random_list.copy())
        random.shuffle(list_of_lists[i])


    lists1, lists2, lists3, lists4 = copy.deepcopy(list_of_lists), copy.deepcopy(list_of_lists), copy.deepcopy(list_of_lists), copy.deepcopy(list_of_lists)

    total_time = 0
    for i in range(10):
        l = lists1[i]
        start = perf_counter()
        heapsort(l)
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(time, "heapsort", n, k)

    total_time = 0
    for i in range(10):
        l = lists1[i]
        start = perf_counter()
        mergesort(l)
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(time, "mergesort", n, k)

    total_time = 0
    for i in range(10):
        l = lists1[i]
        n = len(l)
        start = perf_counter()
        quicksort(l)
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(time, "quicksort", n, k)

    total_time = 0
    for i in range(10):
        l = lists1[i]
        start = perf_counter()
        l.sort()
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(time, "python", n, k)
    


def evaluatepartial(n, k):
    random_list = random.sample(range(0, 1000000), n - k)
    for i in range(k):
        random_list.append(random.choice(random_list[0: n - k - 1]))

    list_of_lists = []
    for i in range(10):
        list_of_lists.append(random_list.copy())
        for j in range(n//20):
            pair = random.sample(range(0, n), 2)
            a = pair[0]
            b = pair[1]
            list_of_lists[i][a], list_of_lists[i][b] = list_of_lists[i][b], list_of_lists[i][a]

    lists1, lists2, lists3, lists4 = copy.deepcopy(list_of_lists), copy.deepcopy(list_of_lists), copy.deepcopy(
        list_of_lists), copy.deepcopy(list_of_lists)

    total_time = 0
    for i in range(10):
        l = lists1[i]
        start = perf_counter()
        heapsort(l)
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(avg_time, "heapsort", n, k, 'p')

    total_time = 0
    for i in range(10):
        l = lists2[i]
        start = perf_counter()
        mergesort(l)
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(avg_time, "mergesort", n, k, 'p')


    total_time = 0
    for i in range(10):
        l = lists3[i]
        n = len(l)
        start = perf_counter()
        quicksort(l)
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(avg_time, "quicksort", n, k, 'p')

    total_time = 0

    for i in range(10):
        l = lists4[i]
        start = perf_counter()
        l.sort()
        end = perf_counter()
        time = end - start
        total_time += time
    avg_time = total_time / 10
    print(avg_time, "python", n, k, 'p')


def evaluate():
    c = 1
    for k in [0, 20, 70]:
        n = 100
        for i in range(4):
            print(c, ".")
            evaluateall(n, k)
            evaluatepartial(n, k)
            print()
            n *= 10
            k *= 10
            c += 1



evaluate()

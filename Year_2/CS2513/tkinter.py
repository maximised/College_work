# Q3

l = [2,6,2,8,5,8,1, 1, 10, 3, 11, 3, 330, 9, 43, 54, 2]

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

def phase1(mylist):
    n = len(mylist)
    i = 0
    while i < n:
        newadded_index = i
        while mylist[newadded_index] > mylist[(newadded_index-1)//2]:
            mylist[newadded_index], mylist[(newadded_index - 1) // 2] = mylist[(newadded_index - 1) // 2], mylist[newadded_index]
            if newadded_index > 2:
                newadded_index = (newadded_index - 1) // 2
        i += 1

    return mylist


def phase2(heap):
    n = len(heap)
    j = n-1
    while j >= 0:
        i = 0
        heap[i], heap[j] = heap[j], heap[i]
        while (not ((heap[i] > heap[i*2+1]) and (heap[i] > heap[i*2+2]))) and i*2+2 < j:
            if heap[i*2+1] > heap[i*2+2]:
                bigger = i*2+1
            else:
                bigger = i*2+2
            heap[i], heap[bigger] = heap[bigger], heap[i]
            i = bigger

        if i*2+2 >= j:
            break
        j -= 1


def heapsort(mylist):
    phase2(phase1(mylist))




# Q4
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


    lists1, lists2, lists3, lists4 = list_of_lists.copy(), list_of_lists.copy(), list_of_lists.copy(), list_of_lists.copy()

    for i in range(10):
        l = lists1[i]
        start = perf_counter()
        heapsort(l)
        end = perf_counter()
        time = end - start
        print(time, "heapsort", n, k)
        print(l)

        l = lists2[i]
        start = perf_counter()
        mergesort(l)
        end = perf_counter()
        time = end - start
        print(time, "mergesort", n, k)
        print()

evaluateall(10, 3)
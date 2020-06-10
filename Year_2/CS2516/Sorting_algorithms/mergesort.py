def merge(list1, list2, mylist):
    """
        time complexity: O(n*logn)
        space complexity: O(n)
    """
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

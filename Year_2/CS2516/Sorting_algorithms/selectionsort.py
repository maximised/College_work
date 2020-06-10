def selection_sort(mylist):
    """
    Worst case time complexity: O(n**2), n swaps
    Best case time complexity: O(n**2), n swaps
    """
    n = len(mylist)
    i = 0
    while i < n:
        smallest = i
        j = i+1
        while j < n:
            if mylist[j] < mylist[smallest]:
                smallest = j
            j += 1
        mylist[i], mylist[smallest] = mylist[smallest], mylist[i]
        i += 1


########################################################
# test code

l = [4,2,6,8,1]

selection_sort(l)

print(l)
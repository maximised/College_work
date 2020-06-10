def insertion_sort(mylist):
    """
        worst case time complexity: O(n**2) with n**2 swaps
        Best case time complexity: (n) with 0 swaps
    """
    c = 0

    n = len(mylist)
    i = 1
    while i < n:
        j = i-1
        while mylist[i] < mylist[j] and j > -1:
            j -= 1
        #insert i in the cell after j
        temp = mylist[i]
        k = i-1
        while k > j:
            mylist[k+1] = mylist[k]
            k -= 1
        mylist[k+1] = temp
        i += 1

        print(c)
        c += 1
        print(mylist)



##########################################################
# test code

l = [8,15,3,23,7,19,25,4,12,18]

insertion_sort(l)

print(l)
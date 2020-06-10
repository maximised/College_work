def bubble_sort(mylist):
    """
    Worst case time complexity: O(n**2)
    """
    n = len(mylist)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1], mylist[j]


###################################################
# test code

l = [2,5,3,1,7]

bubble_sort(l)

print(l)
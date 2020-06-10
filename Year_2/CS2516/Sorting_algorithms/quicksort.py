import random

def quicksort(mylist):
    """
    Best time complexity: O(n*logn)
    Worst case time complexity: O(n**2)
    Most of the time complexity is O(n*logn)
    """
    
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
                if pivot_value > (list[right_index]):
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




##############################################
# test code
l = [8,15,3,23,7,19,25,4,12,18]

quicksort(l)

print(l)

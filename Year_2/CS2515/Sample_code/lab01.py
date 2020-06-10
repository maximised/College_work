""" Sample solutions to Lab01 for CS2515. """

import time
from time import perf_counter

import random

def read_garda_stations_tuples():
    """ Read and return a list of garda stations. """
    all_stations = []
    file = open('garda_stations.txt', 'r', encoding="utf-8")
    for line in file:
        line = line.replace('\n','')
        new_tuple = tuple(line.split('\t'))
        all_stations.append(new_tuple)
    file.close()
    return all_stations

def copy_list_append(mylist):
    """ Create and return a copy of a list by successive appends. """
    newlist = []
    for element in mylist:
        newlist.append(element)
    return newlist

def copy_list_insert(mylist):
    """ Create and return a copy of a list by successive insertions. """
    newlist = []
    for element in mylist:
        newlist.insert(0,element)
    return newlist

def copy_list_sized(mylist):
    """ Create and return a copy of a list, after reserving space. """
    newlist = [None] * len(mylist)
    pos = 0
    while pos < len(mylist):
        newlist[pos] = mylist[pos]
        pos += 1
    return newlist

def linear_search(mylist, target):
    pos = 0
    while pos < len(mylist):
        if mylist[pos][0] == target:
            return pos
        pos += 1
    return -1

def binary_search(mylist, target):
    if len(mylist) < 1:
        return -1
    found = False
    low = 0
    upp = len(mylist)-1
    while low <= upp and not found:
        mid = (low + upp) //2
        if mylist[mid][0] == target:
            return mid
        else:
            if target < mylist[mid][0]:
                upp = mid-1
            else:
                low = mid+1
    return -1    

def perf_check_call(func, *args):
    start_time = perf_counter()
    result = func(*args)
    end_time = perf_counter()
    print('%f seconds' % (end_time-start_time))

    


    

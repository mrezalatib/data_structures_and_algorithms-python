"""
data structures in python:
    list
    tuple
    set
    dictionary
    string
    queue
    heap
    stack
"""

def list_operations():
    mylist = [1, 2, 3, 4, 5]

    # we can index a list:

    mylist[0] #returns the first element
    mylist[0:3] #returns index 0 to 3 but not including 3
    mylist[-1] #negative index returns list items from end of list

    # we can modify elements using indexing:
    mylist[0] = 55 #first item in list converted from 1 to 55

    # we can add items to lists:
    mylist.append(6) #adds 6 to the end of list
    mylist.insert(1, 66) #at index 1, we want to add 66 and remove last item from list. len of list remains the same
    mylist.extend([9, 10]) #adds this list to end of original list

    # we can remove items from a list:
    mylist.remove(10) #removes 10 from list
    mylist.pop() #removes last element in list
    mylist.pop(0) #removes element @ index 0
    mylist.clear() #empties the list

    # we can search and count elemets in a list:
    mylist.index(3) #returns the index of element 3
    mylist.count(3) #counts all occurences of specified item in list

    # we can sort and reverse lists:
    mylist.sort() #sorts list in ascending order
    sorted_list = sorted(mylist) #sorts list without modifying existing list
    mylist.reverse() #reverses a given list

    # we can join all string items in list into 1 string:
    stringlist =  ["Hey", "there"]
    result = " ".join(stringlist) #output = "Hey there"

    #some other list functions:
    max_value = max(mylist)
    min_value = min(mylist)
    total = sum(mylist) #returns the sum of all items in the list

    
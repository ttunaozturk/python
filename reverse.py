list1 = [[1, 2], [3, 4], [5, 6, 7]]  

def reverse_list(l):
    l.reverse()
    for sublist in l:
        if type(sublist) == list:
            reverse_list(sublist)

reverse_list(list1)
print(list1)
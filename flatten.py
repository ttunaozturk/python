list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []
def flatten(l):
    for sublist in l:
        if type(sublist) == list:
            flatten(sublist)
        else:
            flatten_list.append(sublist)
    return flatten_list

print(flatten(list1))
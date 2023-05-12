def list_unique(list: list)->list:
    new_list= []
    for num in list:
        if num not in new_list:
            new_list.append(num)
    return new_list
list= list_unique([1,1,2,2,3,4,4,5,6,6,7,7,8,8])
print(list)
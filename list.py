import copy
list1=[1,3,4,5,6,7,7]
list3 = copy. deepcopy(list1)
list3[3]=8
list3.append(12)
print(list1,list3)
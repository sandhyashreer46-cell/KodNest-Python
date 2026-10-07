#Normal assignment(Not a copy)
original =[[10,20],[30,40]]
copy = original
copy[0][0] = 100
print(copy)
print(original)

#shallow copy
original =[[10,20],[30,40]]
copy = original.copy()
copy[0][0] = 100
print(copy)
print(original)

#Deep copy
import copy
original =[[10,20],[30,40]]
cpy_list = copy.deepcopy(original)
cpy_list[0][0] = 100
print(cpy_list)
print(original)
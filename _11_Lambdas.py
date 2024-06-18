lst1 = [x  for x in range(10)]; print(lst1)

# def square(num):
#     return num ** 2

# sq = lambda x: x**2

lstTools = []
lstTools.append(lambda x: x**2)
lstTools.append(lambda x: x**3)
lstTools.append(lambda x: x**4)

dt = {x:lstTools[0](x)    for x in lst1}; print (dt)

'''
class Student:
    pass

class Group:
    pass

g1 = Group()    

sort(g1, lambda obj1, obj2 : True if obj1.roll < obj2.roll else False)


def sort(coll, cmp):
    # if o1 < o2:
    if cmp(o1, o2):
        Swap(o1, o2)


x if x < y else y
'''
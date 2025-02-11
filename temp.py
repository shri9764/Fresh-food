# def maindecor(call):
#     def inner(name):
#         if name == 'Python':
#             print(f'Learn {name}')
#         else:
#             call(name)
#     return inner


# @maindecor
# def display(name):
#     print(f'Learn coding {name}')


# display('Java')

# rse = lambda x : list(map(x*2,[2,4,5,6]))

# print(rse)

import copy

list1=[1,2,[3,4,[5]]]

shal = list1.copy()
shal[1] = 5

print(list1,shal)
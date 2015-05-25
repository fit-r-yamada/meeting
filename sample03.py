__author__ = 'N-701'
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 2) + fib(num - 1)
ret = 0
list = []
"""ret = fib(40)
for i in range(0,30):
    list.append(fib(i))
print(list)"""
list = [0,1]
def fibArray(list , num):
    if num >= 2:
        list[num] = list[num-1] + list[num-2]

    return list
ret = fibArray(list , 2)
print(ret)
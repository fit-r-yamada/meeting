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
    ret_list = list
    if num >= 2:
        for i in range(2, num):
            ret_list.append(list[i - 1] + list[i -2])
    return ret_list
ret = fibArray(list , 100)
print(ret)
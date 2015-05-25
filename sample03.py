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
"""ret = fib(40)"""
for i in range(0,30):
    list.append(fib(i))
print(list)
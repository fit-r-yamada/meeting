def sumArray(array, num):
    """
    :param array: for sum array
    :param num: first list number
    :return: sum array
    """
    if num == 9:
        return array[9]
    else:
        return array[num] + sumArray(array, num + 1)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = 0
for num in list:
    ans += num
print(ans)
count = len(list)
answer = 0
while count >= 1:
    answer += list[count - 1]
    count -= 1
print(answer)
ret = sumArray(list, 0)
print(ret)
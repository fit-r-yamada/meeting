alpha = ['a', 'b', 'c', 'd', 'e']
number = [1, 2, 3, 4, 5]
def combineArray(array1, array2):
    ret_array = []
    i = 0
    for i in range(0, len(array1)):
        ret_array.append(array1[i])
        ret_array.append(array2[i])
    return ret_array
string = combineArray(alpha, number)
print(string)
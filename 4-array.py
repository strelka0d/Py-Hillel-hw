array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

non_double_array = []
for i in array:
    if i not in non_double_array:
        non_double_array.append(i)


max1 = max(array)
max2 = max(array.remove(max1))
max3 = max(array.remove(max1, max2))
max_list = [max1, max2, max3]


min_index = array.index(min(array))

reverse_array = array[::-1]


print(non_double_array)
print(min_index)
print(max_list)
print(reverse_array)

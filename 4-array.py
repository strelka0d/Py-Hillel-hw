array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

non_double_array = []
for i in array:
    if i not in non_double_array:
        non_double_array.append(i)

lst_sort = sorted(array)
max3 = lst_sort[-3:]

min_index = array.index(min(array))

reverse_array = array[::-1]

print('1.', non_double_array)
print('2.',  max3)
print('3.', min_index)
print('4.', reverse_array)

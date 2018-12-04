array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
max1 = max(array)
max2 = max(array.remove(max1))
max3 = max(array.remove(max1, max2))
max_list = [max1, max2, max3]
print(max_list)

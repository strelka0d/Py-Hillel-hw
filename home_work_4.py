# TASK-1
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
print('TASK-1')

A = [1, 3, 6, 4, 1, 2]


def min_el_out_A(A):
    max_A = int(max(A))
    if max_A <= 0:
        return 1
    if len(A) == 1:
        return 2 if A[0] == 1 else 1
    for num in range(1, max_A+2):
        if num not in A:
            return num


print(min_el_out_A(A))

# ==========================
# TASK-2
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones
# at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps.
#
# Write a function:
#
# def solution(N)
#
# that, given a positive integer N, returns the length of its longest binary gap.
# The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
# Assume that:
# N is an integer within the range [1..2,147,483,647].
print('TASK-2')

N = int(input('please, put a number'))

print(bin(N))


def solution(N):
    bin_N = str(bin(N))
    max_gap = 0
    counter = 0
    gap = False
    for el in bin_N[2:]:
        if el == '1':
            if max_gap < counter:
                max_gap = counter
            gap = True
            counter = 0
        elif gap:
            counter += 1

    return max_gap


print(solution(N))

# ============================

# TASK-3
# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one
# index, and the last element of the array is moved to the first place. For example, the rotation
# of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the
# first place).
# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
# Write a function:
# def solution(A, K)
# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
# For example, given
#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given
#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]
# Given
#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]
# Assume that:
# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].

print('TASK-3')

lst = [1, 2, 3, 4]
k = 4


def rotate_list(lst, k):
    n = 1
    res = lst[:]
    while n <= k:
        res = [res[-1]] + res[:-1]
        n += 1
    return res


print(rotate_list(lst, k))
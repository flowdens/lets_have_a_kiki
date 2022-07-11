from sys import argv
from functools import reduce
from itertools import count, cycle

# 1

# hours, salary, prem = map(int, argv[1:])
# print(hours * salary + prem)

# 2

# numbers = list(map(int, argv[1:]))
# print([numbers[i] for i in range(len(numbers)) if i != 0 and numbers[i-1] < numbers[i]])

# 3

# print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])

# 4

# l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print([x for x in l if l.count(x) == 1])


# 5

# l =[x for x in range(10, 1001, 2)]
# print(reduce(lambda x, y: x * y, l))

# 6

# def my_count(start, end):
#     for x in count(start):
#         yield x
#         if x == end:
#             break
#
#
# for x in my_count(3, 7):
#     print(x)

def my_cycle(l, times):
    flag = 0
    for x in cycle(l):
        flag += 1
        if flag == times + 1:
            break
        yield x


for x in my_cycle([1,2,3,4,5,6], 10):
    print(x)

# 7

# def fact(n):
#     r = 1
#     yield r
#     for i in range(2, n+1):
#         r *= i
#         yield r
#
#
# for el in fact(10):
#     print(el)

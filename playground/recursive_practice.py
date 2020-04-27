# -*- coding:utf-8 -*-
from random import randint

# # Calc the sum of the list
# l = [1,2,3,4]
# def recursive_sum(l:list) -> int:
# 	if len(l) == 0:
# 		return 0
# 	elif len(l) == 1:
# 		return l[0]
# 	else:
# 		return l[0] + recursive_sum(l[1:])

# result = recursive_sum(l)
# print(result)


# Calc the total number of how many numbers in the list
# def calc_numbers(l:list) -> int:
# 	if not l:
# 		return 0
# 	else:
# 		# return 1 + calc_numbers(l[:-1])
# 		return l.pop()/

# l = [randint(1,20) for i in range(10)]
# result = calc_numbers(l)
# print(result)


# # return the largest number of the list
# def find_big_num(l, max=0):
# 	try:
# 		new = l.pop()
# 		if new > max:
# 			max = new
# 		return find_big_num(l, max)
# 	except:
# 		print("The end")
# 		return max

# l = [1,2,3,4,-1,100]
# result = find_big_num(l)
# print(result)








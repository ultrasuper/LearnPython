# -*- coding: utf-8 -*-
from random import randint
def bubble_sort(l: list) -> list:
	# 升序，从小到大
	for i in range(len(l)):
		# 第二层循环的计数变量（需要排序的长度）
		counter = len(l) - i - 1
		for j in range(counter):
			tmp = 0
			if l[j] > l[j+1]:
				tmp = l[j]
				l[j] = l[j+1]
				l[j+1] = tmp
	return l

my_list = [randint(0,100) for i in range(10)]
print(my_list)
ascending_list = bubble_sort(my_list)
print(ascending_list)


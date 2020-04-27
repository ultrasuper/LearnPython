# -*- coding:utf-8 -*-
from random import randint

def binary_search(l:list, target:int) -> int:
	# return the index of the target number
	if len(l) == 0:
		return None
	low = 0
	high = len(l) - 1
	while low <= high:
		mid = int((low+high)/2)
		if target > l[mid]:
			low = mid
		elif target < l[mid]:
			high = mid
		else:
			return mid
	return None

my_list = [randint(1, 100) for x in range(100)]
my_list = sorted(list(set(my_list)))
print(my_list)

my_target = 72
result = binary_search(my_list, my_target)
if result:
	print(f"the location is {result}")
else:
	print("No such number")
# -*- coding: utf-8 -*-
from random import choice
def quick_sort(l):
	if len(l) <= 1:
		return l
	rand = choice(range(0,len(l)))
	search_list = [i for i in range(len(l)) if i != rand]
	key = l[rand]
	left = []
	right = []
	for i in search_list:
		if l[i] <= key:
			left.append(l[i])
		else:
			right.append(l[i])
	return quick_sort(left) + [key] + quick_sort(right)

l = [1,5,6,2,3,9,7,8]
result = quick_sort(l)
print(result)
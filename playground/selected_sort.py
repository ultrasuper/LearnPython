# -*- coding:utf-8 -*-
from random import randint

def select_sort(l:list) -> list:
	# output = []
	for i in range(len(l) - 1):
		_min = i
		for j in range(i+1, len(l)):
			if l[j] < l[_min]:
				_min = j
		tmp = l[i]
		l[i] = l[_min]
		l[_min] = tmp

	return l

# l = [randint(1,100) for i in range(20)]
l = [100, 88, 70, 99, 50, 63, 72, 46, 21]
# l = list(set(l))
print(l)
l = select_sort(l)
print(l)


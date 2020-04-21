# def my_find(haystack, needle):
# 	for index, letter in enumerate(haystack):
# 		if letter == needle:
# 			return index
# 	return -1

# haystack = "Bananarama!"
# print(haystack.find('a'))
# print(my_find(haystack, 'a'))

#fileter practice
# import math
# def is_sqrt(n):
# 	sq = int(math.sqrt(n))
# 	# return isinstance(sq, int)
# 	return sq*sq == n

# l = [x for x in range(1, 101)]
# l_sq = list(filter(is_sqrt, l))
# print(l_sq)


# # sorted() Practice
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
# 	return t[0]

# def by_score(t):
# 	return t[1]

# L_by_name = sorted(L, key=by_name)
# L_by_score = sorted(L, key=by_score, reverse=True)

# print("by_name:\n{0}".format(L_by_name))
# print("by_score:\n{0}".format(L_by_score))

# # Closure
# return a counter function, return a incremental integer
# def createCounter():
# 	def gt():
# 		n = 0
# 		while True:
# 			n += 1
# 			yield n
# 	g = gt()
# 	def counter():
# 		return next(g)

# 	return counter

def createCounter():
	L = [0]
	def counter():
		L[0] += 1
		return L[0]
	return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')




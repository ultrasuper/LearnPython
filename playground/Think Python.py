def my_find(haystack, needle):
	for index, letter in enumerate(haystack):
		if letter == needle:
			return index
	return -1

haystack = "Bananarama!"
print(haystack.find('a'))
print(my_find(haystack, 'a'))
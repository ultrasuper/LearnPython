def handle_input():
	my_input = input("Pls input the arrays:\n")
	try:
		arrays = my_input.split(',')
		# print(arrays)
		a_len = len(arrays)
		l_total = list()
		for i in range(a_len):
			tmp = arrays[i].split('-')
			start = int(tmp[0])
			end = int(tmp[1])
			l_total.append([start, end])
			# print(l_total)

		# print("before:", l_total)
		l_total.sort()
		# print("sorted:", l_total)
		# print(len(l_total))
		return l_total
	except:
		print("-1")
		exit(0)

def handle_output(l):
	l_output = list()
	# count = len(l)
	
	compare = l[0]
	i = 1
	while i < len(l):
		a1 = compare[0]
		b1 = compare[1]
		a2 = l[i][0]
		b2 = l[i][1]
		if a2 > b1:
			l_output.append(compare)
			# print("original:", compare)
			compare = l[i]
			# print("after:", compare)
		elif a2 == b1:
			compare = [a1, b2]
		elif a2 < b1 and b2 <= b1:
			pass
		else:
			compare = [a1, b2]
		i += 1
		# print("i=", i, compare)
	l_output.append(compare)
	l_output.sort()
	output_string = ''
	for k in range(len(l_output)):
		output_string += str(l_output[k][0]) + '-' + str(l_output[k][1])
		if k < len(l_output) - 1:
			output_string += ','
	print(output_string)


if __name__ == "__main__":
	# testing samples:
	# 1-5,8-9,10-15,2-8
	# 1-5,6-8,8-9
	l = handle_input()
	handle_output(l)









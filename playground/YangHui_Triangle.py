
def triangle(max):
	
	l0 = [1]
	l = [1, 1]
	# if max == 1:
	yield(l0)
		# return
	# if max == 2:
	yield(l)
	n = 2
		# return
	while n < max:
		l = generate_list(l)
		l.insert(0, 1)
		l.append(1)
		yield l
		n += 1
	# yield(l)
	return "Done"


def generate_list(l):
	out = []
	for i in range(len(l) - 1):
		out.append(l[i] + l[i+1])
	return out


if __name__ == "__main__":
	N = 10
	# for i in range(1, N+1):
	# 	print(list(triangle(i))[0])
	for i in triangle(N):
		print(i)



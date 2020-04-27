# Use recursive to implement binary search
def recursive_binary_search(l, target, low, high):
	# low = 0
	# high = len(l) - 1
	mid = int((low + high)/2)
	if l[mid] < target:
		low = mid + 1
	elif l[mid] > target:
		high = mid - 1
	else: # l[mid] == target
		return mid
	return recursive_binary_search(l, target, low, high)

l = [randint(1,20) for x in range(20)]
l = list(set(l))
print(l)
N = 12
if N in l:
	result = recursive_binary_search(l, N, 0, len(l))
	print(result)
else:
	print(f"\n{N} is not in the list")
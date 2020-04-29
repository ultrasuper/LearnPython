# -*- coding:utf-8 -*-
from queue import deque
class Node(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def binary_tree_travesal(root):
	q = deque()
	# if root == None:
	# 	return
	# else:
	# 	if root.left != None:
	# 		print(root.left.val)
	# 	if root.right != None:
	# 		print(root.right.val)
	# 	binary_tree_travesal(root.left)

	# if root.left != None or root.right != None:
	q.append(root)
	check_list = []
	values = []
	while q:
		check = q.popleft()
		if check not in check_list and check is not None:
			values.append(check.val)
			if check.left != None:
				q.append(check.left)
				# print(check.left)
			if check.right != None:
				q.append(check.right)
				# print(check.right)
	print(values)


if __name__ == "__main__":


	root = Node(10,Node(7,Node(5, Node(9), Node(11)), Node(2, Node(15), Node(14))),Node(9, Node(8, Node(2), Node(3)), Node(7, Node(5), Node(8))))
	# print(root.val)
	binary_tree_travesal(root)
	# print(root.left.val)
# fpath = r'E:\Python Projects\playground\@property.py'

# with open(fpath, 'r', encoding='utf-8') as f:
# 	l = f.readlines()
# 	for line in l:
# 		line = line.strip()
# 		print(line)


# StringIO
# from io import StringIO
# f = StringIO('hello\nHi\nGood Bye')
# while True:
# 	s = f.readline()
# 	if s == '':
# 		break
# 	print(s.strip())
# print(f.getvalue())

# Exercise 1
# fpath = r'E:\Python Projects\playground\\'
# from io import StringIO
# import os
# import logging
# logging.basicConfig(level=logging.INFO)

# my_input = input()
# f = StringIO()
# f.write(my_input)
# if f.getvalue() == "dir -l":
# 	# print("right branch")
# 	l = [x for x in os.listdir('.') ]# if os.path.isdir(x)
# 	for my_dir in l:
# 		print(my_dir)
# else:
# 	print("Dir Failed")
# 	logging.info(ValueError("Wrong Input"))


# Exercise 2
import os, os.path

# def search(path):
# 	# print("path:%s"%path)
# 	l = [x for x in os.listdir(path)]
# 	# print(l)
# 	for item in l:
# 		# print(item)
# 		if os.path.isfile(os.path.join(path,item)):
# 			# print("isfile:%s"%item)
# 			if my_string in item:
# 				current_dirs = path.split('\\')[-1]
# 				# print(current_dirs)
# 				print(os.path.join(current_dirs, item))
# 		else:
# 			try:
# 				search(os.path.join(path, item))
# 			except FileNotFoundError as e:
# 				print(e)


import time
def search(path):
	# os.walk(top) 实现
	for root, dirs, files in os.walk(path, topdown=False):
		for file in files:
			if my_string in file:
				# print(root)
				# current_dirs = root.split('\\')[-1]
				# print(os.path.split(root))
				current_dirs = os.path.split(root)[-1]
				print(os.path.join(current_dirs, file))
		for _dir in dirs:
			search(_dir)


my_path = 'E:\\Python Projects'
my_string = 'Python'
start = time.time()
search(my_path)
end = time.time()
period = end - start
print(period)
# print(s)


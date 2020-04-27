# -*- coding: utf-8 -*-
from multiprocessing import Process
import multiprocessing, threading
import os

def run_proc(name):
	print("Run child process %s (%s)"%(name, os.getpid()))

# if __name__ == "__main__":
# 	print("parent process id: %s"%(os.getpid()))
# 	print("child process will start")
# 	for i in range(5):
# 		p = Process(target=run_proc, args=('Test'+str(i), ))
# 		p.start()
# 		p.join()
# 	print("Child process end")


import subprocess
# print("$ nslookup www.python.org")
# r = subprocess.call(['nslookup', 'www.python.org'])
# print("Exit code:", r)

# print(multiprocessing.cpu_count())

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()
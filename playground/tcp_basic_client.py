# -*- coding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 10084)) # arguments for socket connection is in tuple type
# s.send(b"Connection Established")
data = s.recv(1024)
print(data.decode('utf-8'))
datas = [b'Mary', b'jack', b'Tony']
for i in datas:
	s.send(i)
	data = s.recv(1024)
	print(data.decode('utf-8'))
# while True:
# 	data = s.recv(1024)
# 	if data:
# 		print(data.decode('utf-8'))
# 	else:
# 		break
	# d = s.recv(1024)

	
s.send(b'exit')
s.close()

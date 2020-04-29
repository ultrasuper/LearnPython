# -*- coding:utf-8 -*-

import socket
from threading import Thread
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 10084))
s.listen(5)
print("Waiting for connection")

while True:
	sock, addr = s.accept()

	def tcplink(sock, addr):
		print("Accept new connection from %s:%s..."%addr)
		sock.send(b'Welcome')
		while True:
			data = sock.recv(1024)
			time.sleep(1)
			
			if data.decode('utf-8') == 'exit' or not data:
				break
			content = data.decode('utf-8')
			print(content)
			sock.send(("Hello, "+str(content)).encode('utf-8'))
			# sock.send(('Hello, %s!'%data.decode('utf-8')).encode('utf-8'))
		sock.close()
		print("Connection from %s:%s is closed"%addr)

	t = Thread(target=tcplink, args=(sock, addr))
	t.start()




	


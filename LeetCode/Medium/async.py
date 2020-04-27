import asyncio
import threading

# async def hello():
# 	print("hello world")
# 	r = await asyncio.sleep(1)
# 	print("hello again")

# @asyncio.coroutine
# def hello():
# 	print("Hello World!")

# 	r = yield from asyncio.sleep(1)
# 	print("Hello WOrld!")

# # get EventLoop
# loop = asyncio.get_event_loop()
# # exec coroutine
# loop.run_until_complete(hello())
# loop.close()


# @asyncio.coroutine
# def hello():
# 	print('Hello world! (%s)'%threading.currentThread())
# 	yield from asyncio.sleep(1)
# 	print('Hello world! (%s)'%threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# old version before 3.4
@asyncio.coroutine
def wget(host):
	print("wget %s ... " % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET /HTTP/1.0\r\nHost:%s\r\n\r\n'%host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		# if line == b'\r\n':
		# 	break
		if not line:
			print(line)
			break
		line = line.decode('utf-8').rstrip()
		# print('%s header > %s'%(host, line))
		if line:
			print(f'{host} -> HTTP header -> {line}')
	writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# words = "hello"
# print(f"{words} world")

#new version after 3.5
import asyncio
import urllib.parse
import sys

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80)

    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            print(f'HTTP header> {line}')

    # Ignore the body, close the socket
    writer.close()

url = sys.argv[1]
asyncio.run(print_http_headers(url))
# Usage:

# python example.py http://example.com/path/page.html
# or with HTTPS:

# python example.py https://example.com/path/page.html
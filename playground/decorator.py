
import time
import functools
# decorator practice
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		print("begin call")
		start = time.time()
		# ret = fn(*args, **kw)
		end = time.time()
		print("end call")
		print("%s execute in %s ms"%(wrapper.__name__, end-start))
		return fn(*args, **kw)
	return wrapper

@metric
def fast(x, y):
	time.sleep(0.0012)
	return x + y

@metric
def slow(x, y, z):
	time.sleep(0.1234)
	return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
	print("测试失败！")
if s != 7986:
	print("测试失败！")
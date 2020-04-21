### day April 21 - learning notes

map():

map(f, list), return a Iterator

map() 返回的是迭代器

---

reduce()

reduce(f(x,y), list, optional)

reduce 对list的每个元素反复调用f

- `reduce`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算

- ```
  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
  ```

  

---

filter()

filter(f, list) # 用f对list中每个元素进行判断，返回True or False, filter再根据结果过滤掉不符合条件的元素，返回由符合条件的元素组成的新list

注意到`filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list。

---

s.strip() 会去掉字符串头尾的空字符，包括空格和'\n', '\t', '\r'

---

迭代：

默认情况下，dict迭代的是key。

对一个序列实现下标循环：

用枚举enumerate

Python内置的`enumerate`函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身：

---

列表生成式：

[x*x for x in range(1,11)]

for 循环后面还可以加上if判断

[x*x for x in range(1,11) if x%2 == 0]

二层循环

[m+n for m in list_1 for n in list_2]

三层和三层以上则很少用到



for循环可以同时使用多个变量，如字典中，key和value同时使用：

for k,v in d.items():

​    print(k, '=', v)



列表生成式，中if-else怎么用：

[x if x%2 == 0 else -x for x in range(1,11)]

在一个列表生成式中，`for`前面的`if ... else`是表达式，而`for`后面的`if`是过滤条件，不能带`else`。

x 是满足条件时的返回值，同样的，-x是不满足条件时的返回值

---

生成器generator

方法一，列表生成式中，把方括号[]换成圆括号()

(x for x in range(1,11))

方法二，函数定义中包含yield关键字

函数执行中，遇到yield关键字会停止执行，再次执行时，从上次yield开始执行

yield可以print

函数访问下一个元素方法：

1. next()方法
2. **for**循环

获取函数返回值，需要捕获异常，可以用try...except结构去捕获

---

可迭代对象Iterable

可以直接作用于`for`循环的对象统称为可迭代对象：`Iterable`。

- 迭代器
- 可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator`。
- 生成器都是迭代器Iterator，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。
- Iterator对象可以被`next()`函数调用并不断返回下一个数据，直到没有数据时抛出`StopIteration`错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过`next()`函数实现按需计算下一个数据，所以`Iterator`的计算是惰性的，只有在需要返回下一个数据时它才会计算。

---

sorted()排序

sorted(Iterable, key=f, Reverse=False)

##### Reverse=True 表示反序

```python
# sorted() Practice
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

L_by_name = sorted(L, key=by_name)
L_by_score = sorted(L, key=by_score, reverse=True)

print("by_name:\n{0}".format(L_by_name))
print("by_score:\n{0}".format(L_by_score))
```

---

闭包Closure

测试失败，以下为测试代码：

```Python
# # Closure
# return a counter function, return a incremental integer
def createCounter():
	j = 0
	def counter(j):
		j = j + 1
		def handle():
			return j
		return handle
	# fs = []
	# for i in range(1,10):
	# 	fs.append(counter(i))
	# 	return fs[i]
	# fs = (x for x in range(1, 6))
	# for i in fs:
	# 	return counter(next(fs))
	return counter(j)

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
```

测试成功代码：

``` python
# # Closure
# return a counter function, return a incremental integer
# def createCounter():
# 	def gt():
# 		n = 0
# 		while True:
# 			n += 1
# 			yield n
# 	g = gt()
# 	def counter():
# 		return next(g)

# 	return counter

def createCounter():
	# L[0] 相当于C语言里的指针
	L = [0]
	def counter():
		L[0] += 1
		return L[0]
	return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
```



---

lambda函数，匿名函数

关键字`lambda`表示匿名函数，冒号前面的`x`表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写`return`，返回值就是该表达式的结果。

---

装饰器decorator

```Python
import time
import functools
# decorator practice
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		start = time.time()
		ret = fn(*args, **kw)
		end = time.time()
		print("%s execute in %s ms"%(fn.__name__, end-start))
		return ret
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
```

---

functools模块 -- 偏函数 partial function

简单总结`functools.partial`的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

``` python
int2 = functools.partial(int, base=2)
```

``` python
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
```

---

类似`_xxx`和`__xxx`这样的函数或变量就是非公开的（private），不应该被直接引用，比如`_abc`，`__abc`等；


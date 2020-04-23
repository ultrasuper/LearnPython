day April 23 - learning notes

调试

assert 

凡是用`print()`来辅助查看的地方，都可以用断言（assert）来替代：

```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```

`assert`的意思是，表达式`n != 0`应该是`True`，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，`assert`语句本身就会抛出`AssertionError`：

启动Python解释器时可以用`-O`参数来关闭`assert`：

```python
python -O err.py
```

---

logging

把`print()`替换为`logging`是第3种方式，和`assert`比，`logging`不会抛出错误，而且可以输出到文件：

```python
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

```

这就是`logging`的好处，它允许你指定记录信息的级别，有`debug`，`info`，`warning`，`error`等几个级别，当我们指定`level=INFO`时，`logging.debug`就不起作用了。同理，指定`level=WARNING`后，`debug`和`info`就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

`logging`的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

---

设置断点

工具: pdb/IDE

在可能出错的地方，插入断点

用IDE比较方便，常用VS Code, PyCharm

---

单元测试：

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

我们需要引入Python自带的`unittest`模块，编写`mydict_test.py`

```python
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
```

编写单元测试时，我们需要编写一个测试类，从`unittest.TestCase`继承。

以`test`开头的方法就是测试方法，不以`test`开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个`test_xxx()`方法。由于`unittest.TestCase`提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是`assertEqual()`：

```python
self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
```

另一种重要的断言就是期待抛出指定类型的Error，比如通过`d['empty']`访问不存在的key时，断言会抛出`KeyError`：

```
with self.assertRaises(KeyError):
    value = d['empty']
```

而通过`d.empty`访问不存在的key时，我们期待抛出`AttributeError`：

```python
with self.assertRaises(AttributeError):
    value = d.empty
```

---

运行单元测试

```python
if __name__ == '__main__':
    unittest.main()
```

另一种方法是在命令行通过参数`-m unittest`直接运行单元测试：

```
$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。

---

### setUp与tearDown

可以在单元测试中编写两个特殊的`setUp()`和`tearDown()`方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

---

明确地告诉函数的调用者该函数的期望输入和输出。

并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用`...`表示中间一大段烦人的输出。(第一行Traceback和最后一行xxError要写)

```python
# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
```

在命令行运行`python mydict2.py`：

```
$ python mydict2.py
```

什么输出也没有。这说明我们编写的doctest运行都是正确的。

当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行。

---

json序列化

``` python
import json
import os, os.path

class Student(object):
	# def __init__(self, **kw):
	# 	super(Student, self).__init__(**kw)

	# def student_2_dict(self):
	# 	return dict(kw)
	def __init__(self, name, gender, score):
		self._name = name
		self._gender = gender
		self._score = score


	def __call__(self):
		pass

def student_2_dict(d):
	d = {
		'name':d._name,
		'gender':d._gender,
		'score':d._score
	}
	return d

s = Student("Bob", "Male", "88")
my_path = os.path.abspath('.')
with open(os.path.join(my_path, 'dump.txt'), 'w') as f:
	json.dump(s, f, default=student_2_dict)

with open(os.path.join(my_path, 'dump.txt'), 'rb') as ff:
	# j_str = ff.read()
	# s = json.loads(j_str)
	s = json.load(ff)
	print(s)
	print(type(s))
	s_json = json.dumps(s)
	print(s_json)
	print(type(s_json))
```

dumps/loads 针对json字符串进行处理

dump/load 针对json对文件的操作

自定义类型，需要编写转换函数（自定义类到dict）作为default参数

---

操作文件和目录

模块：os, os.path, shutil

os:

- os.listdir('.') # 获取当前目录下所有子目录和文件
- os.walk(folder, topdown=False) #返回值 当前目录root, 子目录集dirnames, 子文件集filenames, 方便进行递归操作

os.path

- os.path.isdir() #常用来判断一个目录下对象是否为目录
- os.path.isfile() # 用来判断是否为文件
- os.path.abspath() # 获取绝对路劲

---

文件读写

打开文件f = open(path, opentype) -> f.read()/write() -> 关闭文件f.close()



with open(filepath, opentype) as f:

​    s = f.read()

with 语句默认会关闭文件

---


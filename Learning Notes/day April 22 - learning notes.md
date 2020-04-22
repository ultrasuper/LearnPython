day April 22 - learning notes

---

type() # 判断类型（变量对应的class的类型）

判断是否是函数，调用模块types中的FunctionType

types.FunctionType

---

isinstance(name, type) # 判断一个对象是否是某种类型

---

hasattr(obj, 'x')

setattr(obj, 'x', value)

getattr(obj, 'x', default)

---

相同名字的对象属性将屏蔽掉类属性

---

给类的实例绑定属性和方法

``` python
s = Student()

s.name = 'Michael'

\# bind a method

def func():

​	pass

from types import MethodType

s.func = MethodType(func, s)
```



给一个实例绑定的方法，对另一个实例是不起作用的：

为了给所有实例都绑定方法，可以给class绑定方法：

```python
>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score
```

---

Python允许在定义class的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

使用`__slots__`要注意，`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。

---

Python内置的`@property`装饰器就是负责把一个方法变成属性调用的：

```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

- `@property`的实现比较复杂，我们先考察如何使用。**把一个getter方法变成属性，只需要加上`@property`就可以了**，此时，`@property`本身又创建了另一个装饰器`@score.setter`，负责把一个setter方法变成属性赋值

- 只定义getter方法，不定义setter方法就是一个只读属性：

---

slots怎么用

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

---

多重继承

一个子类继承多个父类

对于需要`Runnable`功能的动物，就多继承一个`Runnable`，例如`Dog`：

```python
class Dog(Mammal, Runnable):
    pass
```

我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

---

定制类

定制包含参数的类实例

#### 实现`Chain().users('michael').repos`输出`/users/michael/repos`

无图无真相，上代码：

```
class Chain(object):
    def __init__(self, path=''):
       self.__path = path

   def __getattr__(self, path):
       return Chain('%s/%s' % (self.__path, path))

   def __call__(self, path):
       return Chain('%s/%s' % (self.__path, path))

   def __str__(self):
       return self.__path

   __repr__ = __str__

   print(Chain().users('michael').repos) # /users/michael/repos
```

看`定制类`这章教程一直很迷惑，来来回回看了好几天，总算是有点理解。（每天在脑子最清醒的时候返回来学最困惑的）

`Chain().users('michael').repos`这是一串什么东西，链式调用？没学过，分分钟想跳过看下一章。

分解成能看懂的：

```
urls = Chain()    # 初始化一个实例
urls = urls.users    # 查找实例的一个属性
urls = urls('michael)    # 调用一个函数
urls = urls.repos    # 还是实例的属性
```

还原成常规方式就成了最基础的东西。

1.第一步

```
urls = Chain()
```

初始化一个实例，此时`urls`等于``，因为定义了默认值`path=''`；

2.第二步

```
urls = urls.users
```

查找`urls`的属性`users`，没找到定义的属性，那就调用`__getattr__`方法，返回了一个函数调用：

```
def __getattr__(self, users):
    return Chain('%s/%s' % (self.__path, users))
```

这一步调用了`Chain()`，而且把要查找的属性`users`作为参数传递了进去，也就是`Chain(users)`,那么根据`Chain()`的逻辑，最后返回的是：`/users`，然后跟上一步的结果拼接，最终返回：`/users`；

3.第三步

```
urls = urls('michael')
```

每次迷茫都在这一步。举例子理解一下：

```
f = abs
print(f.__name__)    # 'abs'
print(f(-123))    # 123
print(callable(f))    # True
```

由于`f`可以被调用，那就可以称：`f`为可调用对象；

```
def func():
    pass

print(callable(func))    # True
```

函数本身就可以被调用，这点无需质疑，所以函数也是可调用对象；

```
class Test(object):
    def __init__(self):
    pass

print(callable(Test))    # True
```

类本身也是可调用对象，不然怎么生成实例化对象；

```
class Test(object):
    def __init__(self):
    pass

test = Test()
print(callable(test))    # False
```

咦？发现个不一样的，类的实例化对象不可以被调用，那它就仅仅只是个纯粹的对象了；

终于对课程上描述`__call__`的话有所理解了， `对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。`

`你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。` 原来是为了让实例化对象和函数一样可以被使用；

那这一步就简单了，可以抽象的理解为：

```
class urls(Chain):
    def __init__(self, path='/users'):
       self.__path = path

   def __getattr__(self, path):
       return urls(('%s/%s' % (self.__path, path)))

    def __call__(self, path):
       return urls(('%s/%s' % (self.__path, path)))

   def __str__(self):
       return self.__path

   __repr__ = __str__
```

然后调用`urls = urls('michael')`，那么最终返回：`/users/michael`

4.最后一步

```
urls = u.repos
```

它和第二步没什么区别，所以`urls`最终为：`/users/michael/repos`;

### over!

---

\__call__() 方法

callable() 函数

---

枚举类

当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：

```python
JAN = 1
FEB = 2
```

\# 导入Enum类

from enum import Enum

\# 创建新的枚举类

Gender = Enum('Gender', ('Male', 'Female'))

`Enum`可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。

---

`Hello`是一个class，它的类型就是`type`，而`h`是一个实例，它的类型就是class `Hello`。

我们可以**通过`type()`函数动态创建出`Hello`类**，而无需通过`class Hello(object)...`的定义：

要创建一个class对象，`type()`函数依次传入3个参数：

1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数`fn`绑定到方法名`hello`上。

```python
>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
```

---

中文代码开头

```python 
# -*- coding: utf-8 -*-
```

---

错误处理

`try...except...finally...`的错误处理机制

```python
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```

- 可以有多个except，执行匹配到的第一个异常
- 可以在所有except后面添加else, 如果没有发生异常，就会执行else
- finally可以不写，但是有finnally一定会执行
- Python所有的错误类型都继承自`BaseException`，所以在使用`except`时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。

---

用logging记录异常信息，可以输出到文件

Python内置的`logging`模块可以非常容易地记录错误信息：

---

抛出异常：

`raise`语句如果不带参数，就会把当前错误原样抛出。

```python
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```

- Q: 我们明明已经捕获了错误，但是，打印一个`ValueError!`后，又把错误通过`raise`语句抛出去了，这不有病么？
- A: 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

---




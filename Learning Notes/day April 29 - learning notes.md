learning notes - April 29

step 1：浏览器向服务器发出请求

方法：GET 只请求资源；POST,  请求资源+用户数据

路径：/full/name/path

域名：由Host头指定：Host: www.sina.com



step 2: 服务器向浏览器返回HTTP响应

响应代码：200：成功，3xx: 重定向，4xx客户端发送的请求有问题，5xx表示服务端有问题

每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。

HTTP GET请求的格式：

```python
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
```

每个Header一行一个，换行符是`\r\n`。

HTTP POST请求的格式：

```
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
```

当遇到连续两个`\r\n`时，Header部分结束，后面的数据全部是Body。

HTTP响应的格式：

```
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
```

HTTP响应如果包含body，也是通过`\r\n\r\n`来分隔的。请再次注意，Body的数据类型由`Content-Type`头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

---

生成器：

函数是顺序执行，遇到`return`语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用`next()`的时候执行，遇到`yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行。
# class Student(object):
# 	@property 
# 	def score(self):
# 		return self.__score
# 		pass

# 	@score.setter
# 	def score(self, value):
# 		if not isinstance(value, int):
# 			raise ValueError('score must be integer!')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must be within 0 -100!')
# 		self.__score = value 
	

# s = Student()
# s.score = 99
# print(s.score)
# s.score = 89
# print(s.__score)


class Screen(object):
	# __slots__ = ('width', 'height', 'resolution')
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, wid):
		self._width = wid
	
	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, ht):
		self._height = ht
	# _resolution = 786432
	@property
	def resolution(self):
		return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


			
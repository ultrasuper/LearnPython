from enum import Enum
# class Gender(Enum):
# 	Male = 0
# 	Female = 1

class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

# Test 
Gender = Enum('Gender', ('Male', 'Female'))
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
	print("测试通过！")
else:
	print("测试失败！")
print(bart.gender.value)
print(type(Gender))
print(type(Gender.Male))
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

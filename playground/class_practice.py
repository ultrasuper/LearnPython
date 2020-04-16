class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print("%s:%d"%(self.__name, self.__score))




if __name__ == "__main__":
	bart = Student("jack", 99)
	# bart.name = "Jack"
	# print(bart)
	bart.print_score()
	bart.__score = 77
	bart.print_score()
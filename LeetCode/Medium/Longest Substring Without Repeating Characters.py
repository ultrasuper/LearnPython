# Method 1
'''
Time Submitted Status Runtime Memory Language
25 minutes ago	Accepted	676 ms	18.6 MB	python3
'''

# class Solution:
# 	def lengthOfLongestSubstring(self, s: str) -> int:
# 		if len(s) == 0:
# 			return 0
# 		l = []
# 		def handle(ss:str):
# 			if len(ss) == 1:
# 				l.append(ss)
# 				return
# 			my_s =''
# 			for i in range(len(ss)):
# 				if ss[i] not in my_s:
# 					my_s += ss[i]
# 					if i == len(ss) - 1:
# 						l.append(my_s)
# 				else:
# 					l.append(my_s)
# 					# handle(ss[i:])
# 					break
# 				# handle(ss[i:])
# 		for i in range(len(s)):
# 			handle(s[i:])
# 		l = list(set(l))
# 		output = max([len(x) for x in l])
# 		print(l)
# 		return output

#Method 2
'''
Time Submitted Status Runtime Memory Language
a few seconds ago	Accepted	644 ms	525.1 MB	python3

'''
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s) == 0:
			return 0
		l = []
		def handle(ss:str):
			if len(ss) == 1:
				l.append(ss)
				return
			my_s =''
			for i in range(len(ss)):
				if ss[i] not in my_s:
					my_s += ss[i]
					if i == len(ss) - 1:
						l.append(my_s)
				else:
					l.append(my_s)
					repeat_char = ss[i]
					fisrt_index = ss.find(repeat_char)
					# handle(ss[i:])
					handle(ss[fisrt_index + 1:])
					break
		handle(s)
		l = list(set(l))
		output = max([len(x) for x in l])
		print(l)
		return output


if __name__ == "__main__":
	examples = {"abcabcbb":3, "bbbbb":1, "pwwkew":3, "au":2, "dvdf":3}
	s = Solution()
	for k,v  in examples.items():
		print(k)
		calc = s.lengthOfLongestSubstring(k)
		print("calc={0}, real={1}".format(calc, v))
	# r = s.lengthOfLongestSubstring()
	    	




# -*- coding: utf-8 -*-

from queue import deque # deque is bidirectional queue

def is_mongo_seller(name):
	if name[-1] == 'm':
		return True
	else:
		return False

def bfs(graph):
	Q = deque()
	Q += graph["you"]
	check_list = []
	while Q:
		check = Q.popleft()
		if check not in check_list:
			if is_mongo_seller(check):
				print(check, "is a mongo seller")
				check_list.append(check)
				return check
			else:
				Q += graph[check]
				check_list.append(check)
		else:
			print("%s already checked"%check)
	print("No mongo seller in your relations")
	return False

if __name__ == "__main__":
	graph = dict()
	graph["you"] = ["Bob", "Claire", "Alice"]
	graph["Bob"] = ["Anuj", "Peggy"]
	graph["Claire"] = ["Thom", "Jonny"]
	graph["Alice"] = ["Peggy"]
	graph["Anuj"] = []
	graph["Peggy"] = []
	graph["Thom"] = []
	graph["Jonny"] = []

	result = bfs(graph)




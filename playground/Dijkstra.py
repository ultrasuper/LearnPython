# -*- coding:utf-8 -*-

# import 

# graph data structure define
graph = {}
graph['start'] = {}
graph['start']['A'] = 6
graph['start']['B'] = 2
graph['A'] = {}
graph['A']['fin'] = 1
graph['B'] = {}
graph['B']['A'] = 3
graph['B']['fin'] = 5
infinity = float("inf")
graph['fin'] = {} # Attention, fin is a node, a dict

# cost : the cost of every node from start
costs = {}
costs['A'] = 6
costs['B'] = 2
costs['fin'] = infinity

# parent node log
parents = {}
parents['A'] = 'start'
parents['B'] = 'start'
parents['fin'] = None

# array that logs the nodes has been processed
processed = []

def get_lowest_cost_node():
	low_node = None
	low_node_cost = infinity
	for n in costs.keys():
		if costs[n] < low_node_cost and n not in processed:
			low_node_cost = costs[n]
			low_node = n
	return low_node

node = get_lowest_cost_node()
while node is not None:
	cost = costs[node]
	neighbors = graph[node] # dict, include key(node name) and value(weight)
	for n in neighbors.keys():
		if cost + neighbors[n] < costs[n]:
			costs[n] = cost + neighbors[n]
			parents[n] = node
	processed.append(node)
	node = get_lowest_cost_node()

print("lowest cost to fin is %s"%costs['fin'])
print("parent node of fin is %s"%parents['fin'])
my_node = 'fin'
my_path = [my_node]
par = my_node
while par != 'start':
	par = parents[par]
	# print(par)
	my_path.insert(0, par)

print(my_path)

path_with_weight = []
for i in range(len(my_path)):
	if my_path[i] is not 'fin':
		path_with_weight.append(my_path[i])
		weight = graph[my_path[i]][my_path[i+1]]
		path_with_weight.append(weight)
	else:
		path_with_weight.append('fin')
output = ''
for j in path_with_weight:
	output += str(j)
	if j != 'fin':
		output += '-->'
print(output)


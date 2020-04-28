# -*- coding: utf-8 -*-
# 背包问题

width = 6
bag = []
water = {}
water['water'] = [dict(val=0, item=set()) for i in range(width)]
bag.append(water)
book = {}
book['book'] = [dict(val=0, item=set()) for i in range(width)]
bag.append(book)
food = {}
food['food'] = [dict(val=0, item=set()) for i in range(width)]
bag.append(food)
jacket = {}
jacket['jacket'] = [dict(val=0, item=set()) for i in range(width)]
bag.append(jacket)
camera = {}
camera['camera'] = [dict(val=0, item=set()) for i in range(width)]
bag.append(camera)

items = ["water", "book", "food", "jacket", "camera"]

weight = {}
weight["water"] = 3
weight["book"] = 1
weight["food"] = 2
weight["jacket"] = 2
weight["camera"] = 1

value = {}
value["water"] = 10
value["book"] = 3
value["food"] = 9
value["jacket"] = 5
value["camera"] = 6


# print(list(bag.keys())[0])
if __name__ == "__main__":
	# print(bag)
	for i in range(len(bag)):

		for j in range(width):
			key = items[i]
			# cell = bag[i][key][j]
			limit = 0
			if weight[key] <= j+1:
				limit = value[key]
				# print(i, j , limit)
			if i != 0:
				weight_limit = j + 1
				weight_left =  weight_limit - weight[key]
				last_key = items[i-1]
				buff = 0
				if weight_left > 0:	
					# bag[i-1][last_key][weight_left - 1]				
					buff= bag[i-1][last_key][weight_left - 1]['val']
					bag[i][key][j]['item'] |= bag[i-1][last_key][weight_left - 1]['item']
				limit += buff
				# last_cell = (list(bag[i-1].values())[j]
				last_cell = bag[i-1][last_key][j]['val']
				if limit > last_cell:
					bag[i][key][j]['val'] = limit
					bag[i][key][j]['item'].add(key)
				else:
					bag[i][key][j]['val'] = last_cell
					bag[i][key][j]['item'] = bag[i-1][last_key][j]['item']
			elif i == 0:
				bag[i][key][j]['val'] = limit
				# bag[i]['items'].add(key)
				bag[i][key][j]['item'].add(key)

	# for b in bag:
	# 	# print(list(b.keys()), list(b.values())[0])
	# 	print(b)
	best_portfolio = bag[-1][items[-1]][-1]
	print(best_portfolio['item'], best_portfolio['val'])








# -*- coding: utf-8 -*-

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set()

states_needed = set()
for k in stations.keys():
	states_needed |= stations[k]
# print(states_needed)

while states_needed:
	best_state = None
	states_covered = set()
	for station, states in stations.items():
		if station not in final_stations:
			covered = states_needed & states
			if covered > states_covered:
				states_covered = covered
				best_state = station
	states_needed -= states_covered
	final_stations.add(best_state)
print(final_stations)


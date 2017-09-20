def traffic_count(array):
	max_arr = [["4:00pm"],["5:00pm"],["6:00pm"],["7:00pm"]]
	for hour in range(0, 4):
		current_hour_traffic = array[(hour*6):(hour*6 + 6)]
		max_arr[hour].append(max(current_hour_traffic))

	traffic_tuples = list(map(lambda x : tuple(x), max_arr))
	return traffic_tuples
    	
	
	
    	

a1 = [23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93]

traffic_count(a1)
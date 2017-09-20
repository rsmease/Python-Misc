import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

tallest_height = 0
tallest_count = 0

for candle in range(n):
	if height[candle] > tallest_height:
		tallest_count = 1
		tallest_height = height[candle]
	elif height[candle] == tallest_height:
		tallest_count += 1
	else:
		pass

print tallest_count
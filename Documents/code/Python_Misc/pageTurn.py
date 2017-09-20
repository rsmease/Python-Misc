import sys

def solve(n, p):
	starting_position = 0
	if (p - n) <= (n - 1):
		starting_position = p
	else:
		starting_position = 1

	turn_count = 0
	page_number = starting_position

	if starting_position == 1:
		while page_number < n:
			turn_count += 1
			page_number += 2
	else:
		if p % 2 != 0:
			page_number -= 1
		while page_number > n:
			turn_count += 1
			page_number -= 2

	return turn_count


p = int(raw_input().strip())
n = int(raw_input().strip())	
print solve(n,p)
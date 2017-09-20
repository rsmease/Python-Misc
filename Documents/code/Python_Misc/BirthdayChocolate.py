import sys

len_chocolate_bar = int(raw_input())
chocolate_bar = map(int, raw_input().split())
chunk_sum, len_chunk = map(int, raw_input().split())

acceptable_chunks = 0

for i in range(0, (len_chocolate_bar - len_chunk + 1), 1):
	chunk = chocolate_bar[i:i+len_chunk]
	if sum(chunk) == chunk_sum:
		acceptable_chunks += 1

print acceptable_chunks


def duck_duck_goose(players, goose):
	goose_index = (len(players) % goose) - 1
	return players[goose_index].name

print duck_duck_goose(["a", "b", "c", "d"], 1)
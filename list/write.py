def write(ls, sep = " ", end = "\n"):
	if type(ls) == type(list()):
		for i in range(len(ls) - 1):
			print(ls[i], end = sep)
		if len(ls):
			print(ls[len(ls) - 1], end = end)
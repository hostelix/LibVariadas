def list_chunk(list, size):
	if len(list) and size != 0:
		return [input[i : i + size] for i in range(0, len(input), size)]
	else:
		return None


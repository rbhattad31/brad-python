def hyphen_sequence(words):
	words_split = words.split("-")
	words_split.sort()
	return "-".join(words_split)
n = input()
result = hyphen_sequence(n)
print(result)
def num_words(file):
	words = file.split()
	return len(words)

def character_count(file):
	char_dict = {}
	for s in file.lower():
		char_dict[s] = char_dict.get(s, 0) + 1
	return char_dict

def sorted_dict(d):
	sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
	return sorted_items

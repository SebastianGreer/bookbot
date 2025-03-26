import sys
from stats import num_words, character_count, sorted_dict

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents

def main():
	text = get_book_text(book_path)
	num_of_words = num_words(text)
	char_dict = character_count(text)
	sorted_chars = sorted_dict(char_dict)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ---------")
	print(f"Found {num_of_words} total words")
	print("--------- Character Count -------")
	for k, v in sorted_chars:
		if k.isalpha():
			print(f"{k}: {v}")
	print("============= END ===============")


main()

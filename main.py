import sys
from stats import get_num_words, count_characters, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()


def main(path_to_file):
    book_text = get_book_text(path_to_file)
    count = get_num_words(book_text)  # Count the number of words in the book text
    char_count = count_characters(book_text)  # Count the characters in the book text
    sorted_list = sort_on(char_count)  # Sort the character counts
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        for char, count in item.items():
            print(f"{char}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]

main(path_to_file)
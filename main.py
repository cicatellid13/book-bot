from stats import word_counter, char_counter, sort_dict
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = word_counter(book_text)
    char_data = char_counter(book_text)
    char_report = sort_dict(char_data)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for info in char_report:
        print(f"{info["char"]}: {info["num"]}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
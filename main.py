from stats import count_words, count_letters, sorted_letters
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    text = get_book_text(file_path)
    print('----------- Word Count ----------')
    count_words(text)
    print('----------- Character Count ----------')
    letters_dict = count_letters(text)
    sorted_letters_dict = sorted_letters(letters_dict)
    for letter, count in sorted_letters_dict:
        print(f"{letter}: {count}")
    print('============= END ===============')
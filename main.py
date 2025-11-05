from stats import get_book_words, get_book_text, get_char_count
import sys

def main():
    # Check command-line arguments first
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # The second argument is the book path
    filepath = args[1]

    # Read and analyze the book
    contents = get_book_text(filepath)
    word_count = get_book_words(contents)
    char_count = get_char_count(contents)

    # Print results
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words.')
    print('--------- Character Count -------')
    for char, count in char_count.items():
        print(f'{char}: {count}')

main()

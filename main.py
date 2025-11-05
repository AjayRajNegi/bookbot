from stats import get_book_words, get_book_text, get_char_count

def main():
    filepath = 'books/frankenstein.txt'
    contents = get_book_text(filepath)
    word_count = get_book_words(contents)
    # print(f"Found {word_count} total words.")
    
    char_count = get_char_count(contents)
    # print("\nCharacter counts:")
    print(char_count)  

main()

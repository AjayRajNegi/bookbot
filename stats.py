def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_words(text):
    words = text.split() 
    return len(words)

def get_char_count(text):
    text = text.lower()
    text = text.replace(" ","")
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
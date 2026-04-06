def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_file):
    book_text = get_book_text(path_to_file)
    return len(book_text.split())

if __name__ == "__main__":
    num_words = get_num_words("books/frankenstein.txt")
    print(f"Found {num_words} total words.")
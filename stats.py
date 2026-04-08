def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_file):
    book_text = get_book_text(path_to_file)
    return len(book_text.split())

def get_char_count(path_to_file):
    book_text = get_book_text(path_to_file)
    char_count = len([c for c in book_text if c != " " and c != "\n"])
    return char_count
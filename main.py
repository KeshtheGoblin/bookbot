  
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {len(book_text.split())} total words.")
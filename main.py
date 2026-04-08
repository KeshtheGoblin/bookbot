from stats import get_char_count, get_num_words


if __name__ == "__main__":
    num_words = get_num_words("books/frankenstein.txt")
    print(f"Found {num_words} total words.")
    char_count = get_char_count("books/frankenstein.txt")
    print(f"{char_count} individual characters (not counting spaces or newlines).")

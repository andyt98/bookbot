import string


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words_count = count_words(text)
    char_counts = count_characters(text)
    print_report(words_count, char_counts)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    lowercase_text = text.lower()
    char_count = {}

    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def print_report(words_count: int, char_counts: dict) -> None:
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(words_count) + " words found in the document\n")
    for k,v in char_counts.items():
        print(f"The '{k}' character was found {v} times")

main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = len(text.split())
    dictionary = sort_characters(text)
    return report(dictionary, num_words)

def report(sorted_dictionary, word_count):
    book_title = "Frankenstein"
    print(f"My Report of {book_title}")
    print(f"This book contained {word_count} words.")
    for letter in sorted_dictionary:
        letter_count = sorted_dictionary[letter]
        if letter.isalpha():
            print(f"The '{letter}' character appeared {letter_count} times.")
    print(f"That concludes my book report of {book_title}.")

def sort_characters(word_string):
    sorted_letters = {}
    uncapped_string = word_string.lower()
    for letter in uncapped_string:
        if letter in sorted_letters:
            sorted_letters[letter] += 1
        else:
            sorted_letters[letter] = 1
    return sorted_letters

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
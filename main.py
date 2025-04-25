from stats import count_words
from stats import count_chars
from stats import report
import sys

#Checks if sys.argv has at least 2 elements
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

# This is a simple program to read a text file and print its contents.
def get_book_text(file):
    with open(file) as f:
        text = f.read()
    return text


def main():
    # Get the text of the book
    # The text file should be in the same directory as this script
    # or provide the full path to the file
    output = get_book_text(book_path)
    
    num_words = count_words(output)
    num_chars = count_chars(output)
    final_report = report(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    #Loop through sorted report to print each character count
    for char_dict in final_report:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()


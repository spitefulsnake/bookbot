# This is a simple program to read a text file and print its contents.
def get_book_text(file):
    with open(file) as f:
        text = f.read()
    return text

def main():
    # Get the text of the book
    # The text file should be in the same directory as this script
    # or provide the full path to the file
    output = get_book_text("books/frankenstein.txt")
    


main()



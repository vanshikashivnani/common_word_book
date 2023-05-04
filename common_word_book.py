import requests

def save_book(url="https://www.gutenberg.org/files/19002/19002-0.txt"):
    """
    Download s book from a URL and save it to a book.txt
    :param url: 
    :return: 
    """
    r = requests.get(url)
    with open("book.txt", "w") as f:
        f.writer(r.text)

def count_words(filename="book.txt"):
    """
    count the words in a book
    :param filename:
    :return:
    """
    words = {}
    with open("book.txt", "r") as f:
        for line in f:
            print(f"Line: {line}")

count_words()


# Library Catalogue Management System

FILE = "books.txt"


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    with open(FILE, "a") as file:
        file.write(book_id + "," + title + "," + author + "\n")

    print("Book added successfully!")


def read_books():
    books = []

    with open(FILE, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                details = line.split(",", 2)

                if len(details) == 3:
                    books.append(details)

    return books


def search_title():
    title = input("Enter title to search: ").strip()
    books = read_books()
    found = False

    for book in books:
        if book[1].lower() == title.lower():
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            found = True

    if not found:
        print("Book not found.")


def search_author():
    author = input("Enter author name: ").strip()
    books = read_books()
    found = False

    for book in books:
        if book[2].lower() == author.lower():
            print(book[0], "-", book[1], "-", book[2])
            found = True

    if not found:
        print("No books found for this author.")


def total_books():
    books = read_books()
    print("Total number of books:", len(books))


def author_report():
    author = input("Enter author name for report: ").strip()
    books = read_books()
    count = 0

    print("\nBooks written by", author, ":")

    for book in books:
        if book[2].lower() == author.lower():
            print(book[0], "-", book[1])
            count += 1

    print("Total books by this author:", count)


# Create the file if it does not exist
with open(FILE, "a"):
    pass


while True:
    print("\n--- LIBRARY CATALOGUE ---")
    print("1. Add Book")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Total Number of Books")
    print("5. Report by Author")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_title()
    elif choice == "3":
        search_author()
    elif choice == "4":
        total_books()
    elif choice == "5":
        author_report()
    elif choice == "6":
        print("Exiting Library Catalogue. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

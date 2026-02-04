import json
FILE_NAME = 'books.json'
#file Handling functions
def load_books():
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError,
            json.JSONDecodeError):
        return []
def save_books(books):
    with open(FILE_NAME, 'w') as f:
        json.dump(books, f, indent=4)
def generate_book_id(books):
    if not books:
        return "B1001"
    last_id = max(int(book["id"][1:])for book in books)
    return f"B{last_id + 1}"
#Library management functions
def find_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None
def add_book(books):
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    if not title or not author:
        print("Title and Author cannot be empty.")
        return
    book_id = generate_book_id(books)
    new_book = {"id": book_id,
                "title": title,
                "author": author,
                "available": True
                }
    books.append(new_book)
    save_books(books)
    print(f"Book added successfully!ID = {book_id}")
def view_books(books):
    if not books:
        print("No books found in library.")
        return
    for book in books:
        status = "Available" if book["available"] else "borrowed"
        print(f"{book['id']} | {book['title']} | {book['author']} | {status}")
def search_book(books):
    book_id = input("Enter Book ID: ")
    book = find_book(books, book_id)

    if book:
        print("book found:")
    else:
        print("Book not found.")

def delete_book(books):
        book_id = input("Enter Book ID to delete: ")
        book = find_book(books, book_id)

        if not book:
          print("Book not found.")
          return
        books.remove(book)
        save_books(books)

        print("Book deleted successfully!")
def borrow_book(books):
    book_id = input("Enter Book ID to borrow: ")
    book = find_book(books, book_id)

    if not book:
        print("Book not found.")
        return
    if not book["available"]:
        print("Book is already borrowed.")
        return
    book["available"] = False
    save_books(books)
    print("Book borrowed successfully!")

def return_book(books):
        book_id = input("Enter Book ID to return: ")
        book = find_book(books, book_id)

        if not book:
            print("Book not found.")
            return
        if book["available"]:
            print("Book was not borrowed.")
            return
        book["available"] = True
        save_books(books)
        print("Book returned successfully!")
def counting_books(books):
    print(f"Total books in library: {len(books)}")
def view_available_books(books):
    available_books = [b for b in books if b["available"]]
    if not available_books:
        print("No available books in library.")
        return
    for book in available_books:
        print(f"{book['id']} | {book['title']} | {book['author']}")
def main():
    books = load_books()
    while True:
       print("\n--- Library Management System ---")
       print("1. Add Book")
       print("2. View Books")
       print("3. Search Book")
       print("4. Delete Book")
       print("5. Borrow Book")
       print("6. Return Book")
       print("7. Count Books")
       print("8. View Available Books")
       print("9. Exit")

       choice = input("Choose an option: ")
       if choice == "1":
         add_book(books)
       elif choice == "2":
         view_books(books)
       elif choice == "3":
         search_book(books)
       elif choice == "4":
         delete_book(books)
       elif choice == "5":
         borrow_book(books)
       elif choice == "6":
         return_book(books)
       elif choice == "7":
         counting_books(books)
       elif choice == "8":
         view_available_books(books)
       elif choice == "9":
          save_books(books)
          print("Goodbye!")
          break
       else:
          print("Invalid choice. Try again.")
if __name__ == "__main__":    
    main()    
       
                      
    
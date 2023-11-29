print ("'Book Store Services'")
class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

class Bookstore:
    books = []
    
    def add_book(self, book):
        self.books.append(book)
        print("Book added to the inventory.")

    def remove_book(self, title):
        if title == title:
        
            for book in self.books:
                self.books.remove(book)
                print("Book have been removed")

        else:
            print("book not found in the inventory")

    def search_by_author(self, author):
        book_found = False
        for book in self.books:
            if book.author.lower() == author.lower():
                print(f"Book by the author: {book.title}")
                
            else:
                print("Book not found")

    def search_by_title(self, title):
        #book_found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"founded book Name : {book.title}")
               
            else:
                print("Book not found")

    def display_book(self):
        for book in self.books:
            print(book.title)

class User:
    books_collection = []
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address



    def display_books_collection(self):
        print(f"Books owned by {self.name}:")
        for book in self.books_collection:
            print(f"{book.title} by {book.author}")

    def Buy_Book(self, book, inventory):
        books_inventory = []
        if book in inventory:
            self.books_collection.append(book)
            print (inventory)
            inventory.remove(book)
            
            print(f"{self.name} bought '{book.title}' by {book.author}")
        else:
            print("Book not available.")


def main():
    while(True):
        bookstore = Bookstore()
        
        print("input a choice from the following choices")
        print("For adding the book press 1")
        print("For removing the book press 2")
        print("Search book by title press 3")
        print("Search book by author name press 4")
        print("Display the book in the inventory press 5")
        print("Quit the program press 6")

        choice = input("Type your choice: ")
        if choice == "1":
            a = input("Add the title of the Book: ")
            b = input("Add the author name of the Book: ")
            c = input("Add the genre of the Book: ")
            d = int(input("Add the price of the Book: "))
            e = int(input("Add the qunatity of the Book: "))

            book3 = Book(a, b, c, d, e)

            bookstore.add_book(book3)

        elif choice == "2":
                removing_book = input("Enter the title of the book: ")
                bookstore.remove_book(removing_book)

        elif choice == "3":
                search_title = input("Enter the title for search the book")

                found_book = bookstore.search_by_title(search_title)

        elif choice == "4":
                search_author = input("Enter the author name for search the book")

                found_book = bookstore.search_by_author(search_author)

        elif choice == "5":
                if bookstore.books:
                    bookstore.display_book()
                else:
                    print("no book found in the inventory")

        elif choice == "6":
        
            print("Program finished")
            break
        else:
            print("invalid choice")

book1 = Book("Python", "Naveed", "Programming", 250, 5)
book2 = Book("Soft Skills", "Mohsin", "Communication", 150, 5)
book3 = Book("Soft Skills-2", "Kainait", "Communication2", 200, 5)

books_inventory = [book1, book2, book3]

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_address = input("Enter your address: ")

user = User(user_name, user_age, user_address)

print("Available books:")
for i, book in enumerate(books_inventory, 1):
    print(f"{i}. {book.title} by {book.author} - Rs{book.price}")

choice = int(input("Enter the number of the book you want to buy: ")) -1

if 0 <= choice < len(books_inventory):
    selected_book = books_inventory[choice]
    user.Buy_Book(selected_book, books_inventory)
else:
    print("Invalid choice.")

user.display_books_collection()

main()        



#buys_book()
#library management
#steps to make a library
# 1. Make a class of library
# 2. Library class include few abstraction like:
#     2.1 Display available books
#     2.2 To lend a book
#     2.3 To add a book
# 3. Make a class of customer
# 4. class of customer includes few abstraction listed below
#     4.1 request for a book
#     4.2 return a book
# 5. Update the library with recent changes
class Library:
    def __init__(self,listsofBooks):
        self.availableBooks = listsofBooks
        
    def displayAvailableBooks(self):
        print()
        print('Available Books: ')
        for book in self.availableBooks:
            print(book)

    def lendBooks(self,requestedBooks):
        if requestedBooks in self.availableBooks:
            print('You have now borrowed the book')
            self.availableBooks.remove(requestedBooks)
        else:
            print('Sorry, the book is not available in our list.')

    def addBooks(self, returnedBooks):
        self.availableBooks.append(returnedBooks)
        print('You have returned the books, Thank you!')
        

class Customer:
    def requestBooks(self):
        print("Enter the name of the book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBooks(self):
        print('Enter the name of the book which you are returning: ')
        self.book = input()
        return self.book


library = Library(['Rich Dad Poor Dad','Think and Grow Rich','The Great Gatsby','For one More Day','In search of Lost time'])
customer = Customer()
while True:
    print('Enter 1 to display all the available books')
    print('Enter 2 to request for the book')
    print('Enter 3 to return the book')
    print('Enter 4 to EXIT')
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBooks = customer.requestBooks()
        library.lendBooks(requestedBooks)
    elif userChoice is 3:
        returnedBooks = customer.returnBooks()
        library.addBooks(returnedBooks)
    elif userChoice is 4:
        quit()
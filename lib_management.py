#library management
class Library:
    def __init__(self,listsofBooks):
        self.availableBooks = listsofBooks
        
    def displayAvailableBooks(self,listsofbooks):
        print()
        print('Available Books: ')
        for book in self.availableBooks:
            print(book)

    def lendBooks(self,requestedBooks):
        if requestedBooks in self.availableBooks:
            print('You have now borrowed the book')
            self.availableBooks.remove(availablebooks)
        else:
            print('Sorry, the book is not available in our list.')

    def addBooks(self, returnBooks):
        self.availableBooks.append(returnBooks)
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
print('Enter 1 to display all the available books')
print('Enter 2 to request for the book')
print('Enter 3 to return the book')
print('Enter 4 to EXIT')
userChoice = input(input())
if userChoice is 1:
    library.displayAvailableBooks()
elif userChoice is 2:
    requestedBooks = customer.requestBooks()
    library.lendBook()
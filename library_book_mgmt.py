available_books = 10
requested_books = 5
class BookNotAvailableError(Exception):
    pass
try:
    if requested_books > available_books:
        raise BookNotAvailableError("Books are unavailable")
    available_books = available_books - requested_books
except BookNotAvailableError as e:
    print("Books are unavailable:",e)
else:
    print("Books are received")
    print("Remaining books:",available_books)
finally:
    print("Library operation completed")
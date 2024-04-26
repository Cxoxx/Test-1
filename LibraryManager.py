#Initialize empty lists, sets and dictionary
books_list = []
authors_set = set()
books_dict = {}
#add books
books_list.append("Python Programming")
auhtors_set.add("John Smith")
books_dict["Python Promgramming"] = "John Smith"

books_list.append("Data Structure And Algorithms")
auhtors_set.add("Jane Doe")
books_dict["Data Structure And Algorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
auhtors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice JOhnson"
#Search for books
search_title = input("Enter the name of the book to search : ")
if search_title in books_lists:
print(f"book found! Author : {books_dict[search_title]}")
else:
print("Book not found") 
#display all books
print("List of Books: ")
for book in books_lists:
print(book)            
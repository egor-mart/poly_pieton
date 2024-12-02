pages_in_book = 100
str_in_page = 50
symb_in_str = 25
element = 4
B = 1
KB = B * 1024
MB = KB * 1024
memory_in_str = symb_in_str * element
memory_in_page = memory_in_str * str_in_page
book_memory = memory_in_page * pages_in_book
KB = B * 1024
MB = KB * 1024
disk_memory = 1.44 * MB
amount_of_books = disk_memory / book_memory
print(int(amount_of_books))



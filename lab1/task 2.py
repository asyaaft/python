# TODO Найдите количество книг, которое можно разместить на дискете
num_pages=100
rows_per_page=50
chars_per_row=25
disk_capacity=1.44
bytes_per_mb=1024*1024
bytes_per_char=4
page_size=rows_per_page*chars_per_row*bytes_per_char
book_size=num_pages * page_size
num_books=int(disk_capacity*bytes_per_mb/book_size)
print(f"Количество книг, помещающихся на дискету:",num_books)

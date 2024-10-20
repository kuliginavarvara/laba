# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
strings_on_page = 50
symbols_on_string = 25
disk_in_mb = 1.44
disk_in_bytes = disk_in_mb * 1024 * 1024


symbols_on_page = strings_on_page * symbols_on_string
symbols_in_book = symbols_on_page * pages

bytes_in_book = symbols_in_book * 4

books_on_disk = disk_in_bytes / bytes_in_book
print("Количество книг, помещающихся на дискету:", int(books_on_disk))

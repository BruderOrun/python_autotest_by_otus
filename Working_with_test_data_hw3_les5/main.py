import json

import Logics as lo

if __name__ == "__main__":
    users_book = lo.book_count % lo.user_count
    min_count_of_book = int((lo.book_count - users_book) / lo.user_count)
    users_with_books_min = lo.ObjectIterator(lo.list_books, min_count_of_book + 1)
    for i in lo.json_on:
        if users_book != 0:
            i["books"] = users_with_books_min.return_class_counter()
            users_book -= 1
        else:
            users_with_books_min.set_count(min_count_of_book)
            i["books"] = users_with_books_min.return_class_counter()
    with open("result.json", "w") as fl:
        json.dump(lo.json_on, fl, indent=4)

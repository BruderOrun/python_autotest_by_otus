import json
import csv

json_on = []
user_count = 0
book_count = 0
list_books = []


class ObjectIterator:
    def __init__(self, itter_object, counter):
        self.counter = counter
        self.iter_object = iter(itter_object)

    def return_class_counter(self):
        asd = []
        step_cout = 0
        while step_cout < self.counter:
            asd.append(next(self.iter_object))
            step_cout += 1
        return asd

    def set_count(self, new_value):
        self.counter = new_value


with open("files/users.json", "r", encoding="utf-8") as f:
    text = json.load(f)
    for user_dict in text:
        user_count += 1
        for key in list(user_dict):
            if key != 'name' and key != "gender" and key != "address" and key != "age":
                del user_dict[key]
        json_on.append(user_dict)

with open("files/books.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, restkey="data")
    for row in reader:
        book_count += 1
        del row["Publisher"]
        list_books.append(row)

"""Завдання 3.
В програмі phone_book (файл скопіювати в свій репозиторій і вже там редагувати) втілити наступні функції:"""

import pickle
from statistics import mean
from operator import itemgetter

running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567", "birthday": "02-05-1972"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321", "birthday": "10-01-2007"},
             ]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname:    %20s |" % entry["surname"])
    print ("| Name:       %20s |" % entry["name"])
    print ("| Age:        %20s |" % entry["age"])
    print ("| Phone:      %20s |" % entry["phone_number"])
    print ("| Birthday:   %20s |" % entry["birthday"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")
    birthday = input("    Enter birthday: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["birthday"] = birthday
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_birthday_phonebook():
    birthday = (input("    Enter birthday: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["birthday"] == birthday:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name = str(input("    Enter name: "))
    index = 0
    found = False
    while index < len(phone_book):
        if phone_book[index]["name"] == name:
            phone_book.pop(index)
            found = True
        else:
            index += 1
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print("Total number of entries:", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    print(sorted(phone_book, key=itemgetter("age")))


#------------------------------------------------------------------------------
def increase_age():
    up = int(input("    Enter age_up: "))
    for entry in phone_book:
        entry['age'] += up


#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    result = mean(list(map(itemgetter("age"), phone_book)))
    print('Average age of all persons:', result)


#------------------------------------------------------------------------------
def print_first_letter_surname():
    first_letter = str(input("     Enter first letter of surname: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["surname"][0] == first_letter:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     10 - Print first letter surname")
      print("     11 - Find entry by birthday")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '10': print_first_letter_surname,
                  '11': find_entry_birthday_phonebook,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")
            printError(ex)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

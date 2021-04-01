books = []

def get_input():
    print('This a book collection database. Please enter 10 books.')
    for count in range(2):
        record = []
        code = int(input('Please enter the Code between 100 and 999: '))
        while not (code >= 100 and code<= 999 and is_unique(count, code)):
            code = int(input('Please enter the code proprely: '))
        title = input('Please enter the Title: ')
        author = input('Please enter the Author: ')
        year = input('Please enter the Year: ')
        print('\n')
        book_record = str(code) + "_" + title + "_" + author + "_" + year
        write_to_file(book_record)
        record.append(book_record)
        books.append(record)


def is_unique(count, code):
    if count == 0:
        return True
    else:
        return not (code in books[0])


def display_data():
    print(" Book ID | Book Title \t\t | Author \t\t| Year of Publication |")
    for row in range(len(books)):
        print("\t", books[row][0], " |\t\t", books[row][1], "\t\t|", books[row][2], "\t\t |\t\t", books[row][3])


def write_to_file(book_record):
    file=open("Library.txt", "+a")
    file.writelines(book_record)
    file.writelines("\n")
    file.close()

def read_file():
    file=open("Library.txt", "r")
    print("Book ID | Book Title \t\t | Author \t\t| Year of Publication")
    for read_lines in file:
        book_records = read_lines.split("_")
        print(book_records[0],"  ","| ", book_records[1], "\t\t |", book_records[2], "      |", book_records[3])

hash_table = [[] for x in range(10)]

def insert(hash_table, code, title, author, year):
    hash_key = hash(code) % len(hash_table)


def search():
    hash_key = hash(key) % len(hash_table)
    slots = hash_table[hash_key]
    for i. abcd in enumerate(slots):
        a, b, c, d= abcd
        if key == a:
            return b


get_input()
#read_file()

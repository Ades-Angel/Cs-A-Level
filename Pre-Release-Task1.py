books = []

def get_input():
    record = []
    print('This a book collection database. Please enter 10 books.')
    for count in range(2):
        code = int(input('Please enter the Code between 100 and 999: '))
        while not (code >= 100 and code<= 999 and is_unique(count, code)):
            code = int(input('Please enter the code proprely: '))
        title = input('Please enter the Title: ')
        author = input('Please enter the Author: ')
        year = input('Please enter the Year: ')
        print('\n')
        book_record = str(code) + "_" + title + "_" + author + "_" + year
        record.append(book_record)
        books.append(record)
    with open('Book_Collection.txt','a') as file:
        file.writelines("\n")
        file.writelines(book_record)


def is_unique(count, code):
    if count == 0:
        return True
    else:
        return not (code in books[0])


def display_data():
    print(" Book ID | Book Title \t\t | Author \t\t| Year of Publication |")
    for row in range(len(books)):
        print("\t", books[row][0], " |\t\t", books[row][1], "\t\t|", books[row][2], "\t\t |\t\t", books[row][3])
    
get_input()
display_data()

def get_input():
    book_list = []
    print('This a book collection database. Please enter 10 books.')
    for x in range(0,2):
        code = input('Please enter the Code: ')
        title = input('Please enter the Title: ')
        author = input('Please enter the Author: ')
        year = input('Please enter the Year: ')
        print('\n')
        book_record = code + "_" + title + "_" + author + "_" + year
        book_list.append(book_record)
    with open('Book_Collection.txt','a') as file:
        file.writelines("\n")
        file.writelines(book_list)
    for i in book_list:
        print('\n')
        print(book_list[i])


get_input()

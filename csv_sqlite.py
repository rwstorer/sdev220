import csv
import sqlite3
ins_str = '''insert into book values(?,?,?)'''
db = sqlite3.connect('books.db')
curs = db.cursor()
with open('books2.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book['title'], book['author'], book['year'])
        curs.execute(ins_str, (book['title'], book['author'], book['year']))
db.commit()
curs.close()
db.close()
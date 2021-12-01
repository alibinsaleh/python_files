import csv

ABOVE_240 = """
    This book {} is written by: {}
"""

LESS_240 = """
    This book {} is not for braveheart
"""


csv_file = open('books.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    title, author, genre, height, publisher = row
    
    if int(height) > 240:
        msg = ABOVE_240.format(title, author)
    else:
        msg = LESS_240.format(title)

    print('Book genre: {}'.format(genre))
    print('Message:')
    print(msg)

csv_file.close()

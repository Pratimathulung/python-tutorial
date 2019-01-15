import sqlite3

conn = sqlite3.connect('emaildb.sqlite3')
cur = conn.cursor()

print('Connected to db . . .')

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name:')
if len(fname) < 1: fname = 'mbox-short.txt'
file = open(fname)
for line in file:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(email, count) VALUES(?, 1)''', (email,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE email = ? ''', (email,))

    conn.commit()

sqlstr = 'SELECT email, count from Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    email = row[0]
    count = row[1]
    print("Email: ", email, " and Count: ", str(count))

cur.close()

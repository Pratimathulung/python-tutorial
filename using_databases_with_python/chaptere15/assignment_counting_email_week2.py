import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER) ''')

fname = input('Enter filename: ')
if len(fname) < 1: fname = 'mbox-short.txt'
file = open(fname)
for line in file:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    (email_name, organization) = email.split('@')
    cur.execute('''Select count from Counts where org = ?''', (organization,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (organization,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (organization,))

    conn.commit()

sqlstr = 'SELECT org, count from Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    org = row[0]
    count = row[1]
    print("Organization: ", org, "and count: ", count)

cur.close()

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:16:14 2008'
words = line.split()
print(words)
email = words[1]
pieces = email.split('@')
print(pieces)
date = words[5]
spl = date.split(':')
print(spl)


import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen(input('Enter URL:'))
soup = BeautifulSoup(page, 'html.parser')
spans = soup('span')

numbers = []

for span in spans:
    print(span)
    numbers.append(int(span.contents[0]))

print(sum(numbers))
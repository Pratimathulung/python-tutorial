import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')  # 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
repeat = int(input('Enter count: '))  # 4
position = int(input('Enter position: '))  # 3


def getNextTag(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    tags = soup('a')
    tag = tags[position - 1]
    return tag


nextTag = getNextTag(url)
href = nextTag.get('href', None)

for i in range(repeat - 1):
    nextTag = getNextTag(href)
    href = nextTag.get('href', None)
    getNextTag(href)

print(nextTag.contents[0])

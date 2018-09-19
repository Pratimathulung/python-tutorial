import urllib.request
import xml.etree.ElementTree as ET

# url = 'http://py4e-data.dr-chuck.net/comments_105116.xml'
url = input('Enter url:')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
# print('count:',len(counts))
total = 0
for count in counts:
    x = count.find('count').text
    total += int(x)
print(total)
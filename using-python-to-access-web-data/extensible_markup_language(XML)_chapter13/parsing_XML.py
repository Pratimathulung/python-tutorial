import xml.etree.ElementTree as ET

# data = '''<person>
# <name>Pratima</name>
# <phone type="intl">
# +15039604096
# </phone>
# <email hide="yes"/>
# </person>'''
#
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

input = '''<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Pratima</name>
        </user>
        <user x='3'>
            <id>007</id>
            <name>Yogen</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:',len(lst))
for item in lst:
    print('Name:',item.find('name').text)
    print('Id:',item.find('id').text)
    print('Attribute:',item.get('x'))
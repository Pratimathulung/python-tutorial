import xml.etree.ElementTree as ET

data = '''<person>
<name>Pratima</name>
<phone type="intl">
+15039604096
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
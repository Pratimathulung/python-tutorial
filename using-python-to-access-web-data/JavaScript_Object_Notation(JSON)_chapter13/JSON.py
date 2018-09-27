import json

data = '''
{
  "Name": "Pratima",
  "Phone": {
    "type": "intl",
    "number": "+56897547596"
  },
  "email": {
    "hide": "yes"
  }
}
'''

info = json.loads(data)
print('Name:', info['Name'])
print('Hide', info['email']['hide'])


input = '''
[
  {"id" : "001",
  "x" : "2",
  "name" :"Pratima"
  },
  {"id" : "003",
  "x" : "7",
  "name" : "Pratima"
  }
]
'''

info = json.loads(input)
print("User Count:", len(info))

for item in info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('Attribute:', item['x'])

def name():
    return 'I am'


print(name(), 'Pratima')


def greet(language):
    if language == 'nepali':
        return 'Namaste'
    elif language == 'rai':
        return 'Sewa'
    else:
        return 'Hello'


print(greet('rai'), 'Pratima')
print(greet('nepali'), 'Yogen')
print(greet('spanish'), 'Harry')

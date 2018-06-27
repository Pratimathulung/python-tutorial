# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class InOutString():
    def __init__(self):
        self.string = " "

    def get_string(self):
        self.string = input("Enter your words here:")

    def print_string(self):
        print(self.string.upper())

str_object = InOutString()
str_object.get_string()
str_object.print_string()
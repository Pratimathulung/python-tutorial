# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the
# sentence capitalized.

# lines = "Hello \nhow are you?"
# print(lines.upper())


def capitalize(lines):
    result = lines.upper()
    return result
    # return lines.upper()


# print(capitalize("Hello \nhow are you?"))


def input_lines():
    lines = ''
    while True:
        input_line = input()
        if input_line:
            lines += input_line + "\n"
        else:
            break
    return lines


print(capitalize(input_lines()))

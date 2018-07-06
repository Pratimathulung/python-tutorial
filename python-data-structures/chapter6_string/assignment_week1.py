# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
#  Convert the extracted value to a floating point number and print it out.

# text = "X-DSPAM-Confidence:    0.8475"
# num = 0.8475
# find_num = text.find(str(num))
# print(float(text[find_num:]))


def extract_num(text):
    find_num = text.find('0')
    return float(text[find_num:])


print(extract_num("X-DSPAM-Confidence:    0.8475"))

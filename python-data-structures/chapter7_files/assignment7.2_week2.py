# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines
# of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
#  and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.


def compute_average(file_name):
    file = open(file_name)
    count = 0
    total = 0
    average = 0
    for line in file:
        if not line.startswith('X-DSPAM-Confidence: '): continue
        count = count + 1
        num = float(line[line.find('0'):])
        total = num + total
        average = total/count
    return round(average, 12)


file_name = input('Enter your file here:')
print('Average spam confidence:', (compute_average(file_name)))

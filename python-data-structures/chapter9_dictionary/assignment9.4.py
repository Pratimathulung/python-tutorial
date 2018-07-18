# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
#  messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer


def find_address(file_name):
    file = open(file_name)
    result = []
    for line in file:
        if not line.startswith('From') or line.startswith('From:'):
            continue
        else:
            words = line.split()
            result.append(words[1])
    return result


file_name = input('Enter file here:')
emails = find_address(file_name)


def count_email(emails):
    counts = {}
    for email in emails:
        if email not in counts:
            counts[email] = 1
        else:
            counts[email] = counts.get(email, 0) + 1
    return counts


counted_email = count_email(emails)


def highest_count():
    maxval = None
    maxkey = None
    for email, count in counted_email.items():
        if maxval is None or count > maxval:
            maxval = count
            maxkey = email
    return maxkey, maxval


highest_repeated_email = highest_count()
print(highest_repeated_email[0], highest_repeated_email[1])

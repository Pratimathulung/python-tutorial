names = ['csev', 'cwen', 'zqien', 'cwen']
counts = dict()
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)


def count_name(names):
    counts = {}
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts.get(name) + 1
    return counts


print(count_name(['csev', 'cwen', 'zqien', 'cwen']))
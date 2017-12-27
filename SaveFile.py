man = []
other = []

try:
    date = open('sketch', 'w')

    for each_line in date:
        try:
            (role, line_spoken) = each_line.split(":")
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print("The file is missing.")
print(man)
print(other)
print("read done!", file='sketch')
date.close()

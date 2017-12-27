man = []
other = []
# 读取源文件sketch，将说话人和说话内容分别存储
try:
    with open('sketch') as date:
        for each_line in date:
            try:
                (role, line_spoken) = each_line.split(":")
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError as value_err:
                print("value error:" + str(value_err))
except IOError:
    print("The file is missing.")

# 创建两个文件，分别存储说话人和说话内容
try:
    with open('man_file.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_file.txt', 'w') as other_file:
        print(other, file=other_file)
except IOError as io_err:
    print('File error.' + str(io_err))


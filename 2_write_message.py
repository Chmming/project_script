filename = 'test_files\programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I love python\n")
    file_object.write("I love C++\n")
with open(filename) as file_object:
    for line in file_object.readlines():
        lines = line.rstrip()
    print(lines)
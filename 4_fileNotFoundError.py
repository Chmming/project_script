filename = input('Enter your file path and name :')
filename_new = '123.txt'
try:
    with open(filename,encoding = 'utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry,the file" + filename + " does not exist")
else:
    with open(filename_new,'w',encoding = 'utf-8') as  f_new:
        f_new.write(contents)
with open(filename_new,encoding = 'utf-8') as f_new:
    for line in f_new.readlines():
        lines = line.rstrip()
        print(lines)
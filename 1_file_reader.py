#文件路径
'''with open('test_files\hello.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''
#逐行读取
'''
with open('test_files\hello.txt') as file_object:
    for line in file_object:
        print(line.rstrip()) #print(line)打印出来的字符串末尾有空白行，line.rstrip()剥除字符串末尾的空白行
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() #从文件中逐行读取，将其存储在列表lines中。
#打印列表lines中的各行
for line in lines:
    print(line.rstrip())
'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # 从文件中逐行读取，将其存储在列表lines中。
    pi_string = ''
#打印列表lines中的各行
    for line in lines:
        pi_string += line.rstrip()
    print(pi_string)
    birthday = input("Enter your birthday,in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first miilion digits of pi")
    else:
        print("Your birthday do not appears in the first miilion digits of pi")
    for birthday in pi_string:
        birthdays = birthday
    print(birthdays) #？
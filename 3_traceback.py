'''try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
'''
print("Give me two numbers,and I’ll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
            break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        """pass语句，可在代码中使用它来让python什么都不要做"""
        pass #print("You can't divide by zero!")
    else:
        print(answer)
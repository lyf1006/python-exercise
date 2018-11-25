import json
filepath = r'C:\Users\huayu\Desktop\python-exercise\10.4\num.txt'
try:
    with open(filepath) as file_object:
        num = json.load(file_object)
    print("I know your favorite number is :" + num)
except FileNotFoundError:
    num = input("please enter a number: ")
    with open(filepath, 'w') as file_object:
        json.dump(num, file_object)
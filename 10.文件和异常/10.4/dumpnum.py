import json
num = input("please enter a number: ")
filepath = r'C:\Users\huayu\Desktop\python-exercise\10.4\num.txt'
with open(filepath, 'w') as file_object:
    json.dump(num, file_object)
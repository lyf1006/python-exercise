import json
filepath = r'C:\Users\huayu\Desktop\python-exercise\10.4\num.txt'
with open(filepath) as file_object:
    num = json.load(file_object)
print("I know your favorite number is :" + num)
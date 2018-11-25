#replace 方法不会修改原字符串,会替换所有的特定单词
file_path = r'C:\Users\huayu\Desktop\python-exercise\10.1\learning_python.txt'
with open(file_path) as file_object:
    # contexts = file_object.readlines()
    # for line in contexts:
    #     print(line.replace('Python', 'Java').rstrip())
    contexts = file_object.read()
    print(contexts.replace('Python', 'JavaScript'))
"""路径前加r"""
file_path = r'C:\Users\huayu\Desktop\python-exercise\10.1\learning_python.txt'
#读取整个文件
#read方法在读取到文件末尾时返回一个空行
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print("\n")

#遍历文件对象
#文件内容每行之后都有一个换行符，print方法也会自动换行
#因此打印的每行内容之间都有一个多余的空行
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")

#遍历文件对象存入列表
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
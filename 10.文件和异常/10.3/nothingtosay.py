#文件路径由r+' '引起的路径
#沉默的异常
filepath1 = r'C:\Users\huayu\Desktop\python-exercise\10.3\cats.txt'
filepath2 = r'C:\Users\huayu\Desktop\python-exercise\10.3\dog.txt'
try:
    with open(filepath1) as file_object:
        contexts = file_object.read()
        print(contexts)
    with open(filepath2) as file_object2:
        contexts2 = file_object2.read()
        print(contexts2)
except FileNotFoundError:
    pass
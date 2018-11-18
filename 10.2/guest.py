#只能写入字符串，数字需要进行类型转换
#为啥子写完可以读出来，但是我看不见呢
#使用Python工具写入文件，就可以看到的呢
name = input('请输入用户名： ')
file_path = r'C:\Users\huayu\Desktop\python-exercise\10.2\guest.txt'
#写入文件
with open(file_path, 'w')as file_object:
    file_object.write(name)

# with open(file_path) as file_object:
#     contexts = file_object.read()
#     print(contexts)
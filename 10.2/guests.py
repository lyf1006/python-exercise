#写入多行内容注意采用附加模式，以防覆盖内容
file_path = r'C:\Users\huayu\Desktop\python-exercise\10.2\guests.txt'
while True:
    with open(file_path, 'a')as file_object:
        user = input('请输入用户名：')
        if user == 'quit':
            break
        print('Hello, ' + user)
        file_object.write(user + ' is logging.\n')



file_path = r'C:\Users\huayu\Desktop\python-exercise\10.2\reasons.txt'
while True:
    reason = input('请输入你喜欢编程的理由：')
    if reason == 'quit':
        break
    with open(file_path, 'a')as file_object:
        file_object.write(reason + '\n')
    
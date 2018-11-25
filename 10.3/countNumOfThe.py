#count方法计算文件中包含该特定词的个数
#split方法拆分文件内容，可以统计单词个数
filepath = r'C:\Users\huayu\Desktop\python-exercise\10.3\sea.txt'
with open(filepath) as file_object:
    context = file_object.read()
print(context.lower().count('the'))
words = context.split()
print(len(words))
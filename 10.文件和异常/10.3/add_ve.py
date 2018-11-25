num1 = input("请输入一个数字： ")
num2 = input("请再输入一个数字： ")
try:
    sum = int(num1) + int(num2)
except ValueError :
    print("请检查输入内容是否为数字。")
else:
    print(sum)
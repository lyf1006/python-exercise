#making a large T-shirt...
#函数形参指定默认值等号两边不要有空格
def make_shirt(size='large', text='I love Python'):
    print("The size of the T-shirt is :" + str(size))
    print("The text that going to print is :" + text)

make_shirt()
#函数调用参数赋值等号两边不要有空格
make_shirt(size='medium')
make_shirt(text='I love the world!')
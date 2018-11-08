#while 循环中使用测试条件
""" tip = "Please enter an ingrident you want to add: "
tip += "\n(Enter 'quit' when you are finished)"
ingrident=""
while ingrident != "quit":
    ingrident = input(tip)
    if ingrident != 'quit':
        print("We will add "+ingrident+" for you.") """

#使用标志来控制循环
active = 'True'
tip = "Please enter an ingrident you want to add: "
tip += "\n(Enter 'quit' when you are finished)"
while active:
    ingrident = input(tip)
    if ingrident == 'quit':
        active = False
    else:
        print("We will add "+ingrident+" for you.")



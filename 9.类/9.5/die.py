from random import randint
class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

dieone = Die(6)
x = 10

#python 没有++，--运算符
while x > 0:
    dieone.roll_die()
    x -= 1

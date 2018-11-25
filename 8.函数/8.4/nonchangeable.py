#有多个函数时使用两个空行分隔
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    index = 0
    for magician in magicians:
        magicians[index] = "the Great " + magician
        index += 1
    return magicians

magicians = ['Alan', 'Bob', 'Creal', 'David']
copy_magicains = make_great(magicians[:])

show_magicians(copy_magicains)
show_magicians(magicians)
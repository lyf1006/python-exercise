def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    index = 0
    for magician in magicians:
        magicians[index] = "the Great " + magician
        index += 1
    #return magicians

magicians = ['Alan', 'Bob', 'Creal', 'David']
make_great(magicians)
show_magicians(magicians)
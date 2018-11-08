#make albums...
def make_album(name, album_name):
    album = {'name' : name, 'album_name' : album_name}
    return album

while True:
    name = input("Please enter a singer's name: (enter 'quit' to exit)")
    if name == 'quit':
        break
    album_name = input("Please enter a album's name (enter 'quit' to exit)")
    if album_name == 'quit':
        break
    album = make_album(name, album_name)
    print(album)



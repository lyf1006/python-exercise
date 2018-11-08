#make album...
#形参指定默认值时等号两边不要有空格
def make_album(name, album_name, number_of_songs=0):
    if number_of_songs == 0:
        album = {'name' : name, 'album_name' : album_name}
    else:
        album = {'name' : name, 'album_name' : album_name, 'number_of_songs' : number_of_songs}
    return album

album = make_album('zhangjie', 'Me')
print(album)
albumone = make_album('zhanghan', 'friend', '106')
print(albumone)


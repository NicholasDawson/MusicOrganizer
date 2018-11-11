from mutagen.easyid3 import EasyID3
import os
import setup_info
import time

to_be_organized_lst = os.listdir(setup_info.to_be_organized)
destination_lst = os.listdir(setup_info.destination)

for song in to_be_organized_lst:
    if song[-4:] != '.mp3':
        raise TypeError(setup_info.to_be_organized + '/' + song + ' is not an MP3')
    else:
        artist = EasyID3(setup_info.to_be_organized + '/' + song)['artist']
        album = EasyID3(setup_info.to_be_organized + '/' + song)['album']
        title = EasyID3(setup_info.to_be_organized + '/' + song)['title']
        if not os.path.isdir(setup_info.destination + '/' + artist[0]):
            os.makedirs(setup_info.destination + '/' + artist[0])
        if not os.path.isdir(setup_info.destination + '/' + artist[0] + '/' + album[0]):
            os.makedirs(setup_info.destination + '/' + artist[0] + '/' + album[0])
        try:
            os.rename((setup_info.to_be_organized + '/' + song), (setup_info.destination + '/' + artist[0] + '/' + album[0] + '/' + artist[0] + ' - ' + title[0] + '.mp3'))
            print(artist[0] + '-' + title[0])
        except FileExistsError:
            print(artist[0] + '-' + title[0] + ' ALREADY EXISTS')
            os.remove(setup_info.to_be_organized + '/' + song)
            print('DELETED: ' + setup_info.to_be_organized + '/' + song)


print('-----ORGANIZATION COMPLETE-----')
time.sleep(2)












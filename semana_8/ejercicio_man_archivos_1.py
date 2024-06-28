def read_song_name():
    songs = []
    file_name = ('song_names.txt')
    with open(file_name, 'r') as file:
                for line in file.readlines():
                    songs.append(line)
                    songs.sort()
                return songs


def write_txt_file(path):
    with open(path, 'w') as file:
            lines = read_song_name()
            for line in lines:
                file.write(line)
        
write_txt_file('songs_sorted.txt')
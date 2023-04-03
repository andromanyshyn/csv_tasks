import csv

with open(r'C:\Users\Andr\CsvTasks\tik_tok_songs\TikTok_songs_2022.csv', 'r', encoding='utf-8') as file_read:
    with open('album_count_songs.csv', 'w') as file_write:
        d = {}
        reader = csv.DictReader(file_read)
        lst = list(reader)
        songs = [i['track_name'] for i in lst]
        albums = [i['album'] for i in lst]

        songs_albums = list(zip(songs, albums))

        for i in albums:
            for j in songs_albums:
                if i in j:
                    d.setdefault(i, []).append(j[0])
        for b in d.items():
            print(b)

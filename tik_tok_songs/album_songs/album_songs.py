import csv

with open(r'C:\Users\Andrew\csv_tasks\tik_tok_songs\TikTok_songs_2022.csv', 'r', encoding='utf-8') as file_read:
    with open('album_songs.csv', 'w', encoding='utf-8') as file_write:
        d = {}
        reader = csv.DictReader(file_read)
        writer = csv.writer(file_write)

        lst = list(reader)
        albums = [album['album'] for album in lst]

        d = {}
        for album in albums:
            d[album] = [i['track_name'] for i in lst if album == i['album']]
        for k, v in d.items():
            writer.writerow([k, v])

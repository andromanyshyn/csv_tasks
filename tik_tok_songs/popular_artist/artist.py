import csv

with open(r'C:\Users\Andr\CsvTasks\tik_tok_songs\TikTok_songs_2022.csv', 'r', encoding='utf-8') as file_read:
    with open('popular_artist.csv', 'w') as file_write:
        reader = csv.DictReader(file_read)
        lst = list(reader)
        artist_name = [artist['artist_name'] for artist in lst]
        artist_pop = [artist['artist_pop'] for artist in lst]
        most_popular = {k: v for k, v in zip(artist_name, artist_pop) if v == max(artist_pop)}

        writer = csv.writer(file_write)
        writer.writerow(['Most Popular Artist'])
        writer.writerow(list(most_popular))

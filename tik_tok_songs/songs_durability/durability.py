import csv

with open(r'C:\Users\Andr\CsvTasks\tik_tok_songs\TikTok_songs_2022.csv', 'r', encoding='utf-8') as file_read:
    with open('songs_durability.csv', 'w') as file_write:
        reader = csv.DictReader(file_read)
        writer = csv.writer(file_write)
        all_dururation = [int(i['duration_ms']) for i in reader]

        writer.writerow(['Songs Duration'])
        writer.writerow([f'{sum(all_dururation) / 3600000}  hours'])

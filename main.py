import csv
import random


def get_town():
    towns = [
        'Kuiv',
        'Lviv',
        'Dnipro',
        'Xarkiv',
        'Ivano-Frankivsk',
        'Zaporizhya',
        'Ternopil',
        'Odesa',
        'Vinnucia',
        'Lytsk'
    ]

    return random.choice(towns)


with open('sample_clients_data.csv') as file_read:
    with open('client.csv', 'w') as file_write:
        csv_file = csv.reader(file_read)
        lst_csv = list(csv_file)
        lst_csv[0].insert(4, 'town')
        for line in range(1, len(lst_csv)):
            lst_csv[line].insert(4, get_town())

        writer = csv.writer(file_write)
        for line in lst_csv:
            writer.writerow(line)


with open('client.csv') as file:
    csv_file = csv.DictReader(file)
    for line in csv_file:
        print(line)

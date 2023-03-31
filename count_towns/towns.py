import csv

with open(r'C:\Users\Andr\CsvTasks\client.csv') as file_read:
    with open('count_towns.csv', 'w') as file_write:
        reader = csv.DictReader(file_read)
        list_towns = [town['town'] for town in reader]
        towns_dict = {town: list_towns.count(town) for town in list_towns}
        towns = [i for i in towns_dict.keys()]
        counters_towns = [i for i in towns_dict.values()]

        writer = csv.writer(file_write)
        writer.writerow(towns)
        writer.writerow(counters_towns)


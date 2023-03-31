import csv

with open(r'C:\Users\Andr\CsvTasks\client.csv') as file_read:
    with open('longest_name_surname.csv', 'w') as file_write:
        reader = csv.DictReader(file_read)
        list_of_dicts = list(reader)

        firstname = max([firstname['first_name'] for firstname in list_of_dicts], key=len)
        lastname = max([lastname['last_name'] for lastname in list_of_dicts], key=len)

        writer = csv.writer(file_write)
        writer.writerow(['Longest Name', 'Longest Surname'])
        writer.writerow([firstname, lastname])

import csv

with open(r'C:\Users\Andr\CsvTasks\client.csv') as file_read:
    with open('count_emails_com.csv', 'w') as file_write:
        reader = csv.DictReader(file_read)
        lst = [email['email'] for email in reader if email['email'].split('.')[1] == 'com']

        writer = csv.writer(file_write)
        writer.writerow(['Count Emails .com'])
        writer.writerow([len(lst)])


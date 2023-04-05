import csv

with open(r'C:\Users\Andrew\csv_tasks\client.csv') as file_read:
    with open('changed_emails.csv', 'w') as file_write:
        for line in file_read.read().split():
            if '.ru' in line:
                line = line.replace('.ru', '.ua')
            file_write.write(line + '\n')




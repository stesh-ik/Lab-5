import re
import csv

with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    task1_content = file.read()

words_after_comma = re.findall(r'\b\w+,\b', task1_content)
square_bracket_contents = re.findall(r'\[.*?\]', task1_content)


with open('task2.html', 'r', encoding='utf-8') as file:
    task2_content = file.read()

colors = re.findall(r'(#[0-9a-fA-F]{3,6}|rgb\(\d{1,3}, \d{1,3}, \d{1,3}\)|rgba\(\d{1,3}, \d{1,3}, \d{1,3}, [0-9.]+\))', task2_content)


with open('task3.txt', 'r', encoding='utf-8') as file:
    task3_content = file.read()


ids = re.findall(r'\b\d+\b', task3_content)
surnames = re.findall(r'\b[A-Z][a-z]+\b', task3_content)
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', task3_content)
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', task3_content)
websites = re.findall(r'https?://\S+', task3_content)


organized_data = zip(ids, surnames, emails, dates, websites)


with open('organized_task3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['ID', 'Surname', 'Email', 'Registration Date', 'Website'])
    csvwriter.writerows(organized_data)

print(words_after_comma, square_bracket_contents, colors)

import re

file_path = 'task_add.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


date_pattern = r'\s(\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})'
email_pattern = r'\s([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
url_pattern = r'\s(https?://[^\s]+)'


dates = re.findall(date_pattern, file_content)
emails = re.findall(email_pattern, file_content)
urls = re.findall(url_pattern, file_content)


dates = dates[:5]
emails = emails[:5]
urls = urls[:5]
print(dates, emails, urls)

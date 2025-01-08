import re
import csv

# Reading and processing task1-ru.txt
with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    task1_content = file.read()

# Extracting words followed by a comma and contents within square brackets
words_after_comma = re.findall(r'\b\w+,\b', task1_content)
square_bracket_contents = re.findall(r'\[.*?\]', task1_content)

# Reading and processing task2.html
with open('task2.html', 'r', encoding='utf-8') as file:
    task2_content = file.read()

# Extracting color codes (assuming CSS-like color codes or color names in HTML)
colors = re.findall(r'(#[0-9a-fA-F]{3,6}|rgb\(\d{1,3}, \d{1,3}, \d{1,3}\)|rgba\(\d{1,3}, \d{1,3}, \d{1,3}, [0-9.]+\))', task2_content)

# Reading and processing task3.txt
with open('task3.txt', 'r', encoding='utf-8') as file:
    task3_content = file.read()

# Extracting each type of data using regular expressions
ids = re.findall(r'\b\d+\b', task3_content)
surnames = re.findall(r'\b[A-Z][a-z]+\b', task3_content)
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', task3_content)
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', task3_content)
websites = re.findall(r'https?://\S+', task3_content)

# Organizing data into rows
organized_data = zip(ids, surnames, emails, dates, websites)

# Writing to CSV
with open('organized_task3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['ID', 'Surname', 'Email', 'Registration Date', 'Website'])
    csvwriter.writerows(organized_data)

print(words_after_comma, square_bracket_contents, colors)
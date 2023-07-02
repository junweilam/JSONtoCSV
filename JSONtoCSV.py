import json
import csv

json_file = 'D:\\Projects\\ITP_SE_14\\Scraper\\Review_Counts\\Australia Review Counts.json'
csv_file = 'D:\\Projects\\CSVFiles\\Australia.csv'

with open(json_file) as file:
    data = json.load(file)

fieldnames = ['Company', 'Count']

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader

    for item in data:
        for key, value in item.items():
            writer.writerow({'Company': key, 'Count': value})

print(f"CSV file '{csv_file}' has been created successfully.")
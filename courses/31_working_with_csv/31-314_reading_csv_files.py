# conventional read file
# with open('fighters.txt') as file:
#     file.read()

# csv module
from csv import reader, DictReader

# reader - lets you iterate over rows of the CSV as lists
with open("fighters.txt") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)

# DictReader - lets you iterate over rows of the CSV as OrderedDict
with open("fighters.txt") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row['Name'])

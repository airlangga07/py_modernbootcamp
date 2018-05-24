from csv import writer, reader

# with open('cats.csv', 'w') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['Name', 'Age'])
#     csv_writer.writerow(['Blue', 4])
#     csv_writer.writerow(['Kitty', 1])

with open('fighters.txt') as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]
    for row in fighters:
        print(row)

with open('screaming_fighters.csv', 'w') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)
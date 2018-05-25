from csv import DictWriter, DictReader

# with open('cats.csv', 'w') as file:
#     headers = ['Name', 'Breed', 'Age']
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({ 'Name': 'Garfield', 'Breed': 'Orange Tabby', 'Age': 16 })

def cm_to_in(cm):
    return float(cm) * 0.393701

with open('fighters.txt') as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open('inches_fighers.csv', 'w') as file:
    headers = ['Name', 'Country', 'Height']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            'Name': f['Name'],
            'Country': f['Country'],
            'Height': cm_to_in(f['Height (in cm)'])
        })
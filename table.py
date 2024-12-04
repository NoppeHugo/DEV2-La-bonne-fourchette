import csv

# Afficher le statut des tables
def afficher_statut_tables():
    with open('data/tables.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Table {row[0]} - Statut : {row[1]}")

# Fusion de tables
def fusionner_tables(table_ids):
    with open('data/tables.csv', mode='r') as file:
        tables = [row for row in csv.reader(file)]

    for table in tables:
        if table[0] in table_ids:
            table[1] = 'occupée'

    with open('data/tables.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tables)

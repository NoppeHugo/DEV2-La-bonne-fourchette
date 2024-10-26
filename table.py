def ajouter_table(table_id, capacity, status="Available", location=""):
    with open('data/tables.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([table_id, capacity, status, location])
        print(f"Table {table_id} ajoutée avec une capacité de {capacity} personnes.")

# Exemple d'utilisation
ajouter_table(1, 2, "Available", "Near window")

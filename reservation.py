import csv

# Ajouter une réservation
def ajouter_reservation(nom, telephone, date, heure, personnes):
    with open('data/reservations.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nom, telephone, date, heure, personnes])

# Modifier une réservation
def modifier_reservation(telephone, date, nouvelles_informations):
    lignes = []
    with open('data/reservations.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == telephone and row[2] == date:
                lignes.append(nouvelles_informations)
            else:
                lignes.append(row)

    with open('data/reservations.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lignes)

# Annuler une réservation
def annuler_reservation(telephone, date):
    lignes = []
    with open('data/reservations.csv', mode='r') as file:
        reader = csv.reader(file)
        lignes = [row for row in reader if not (row[1] == telephone and row[2] == date)]

    with open('data/reservations.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lignes)

# Afficher les réservations
def afficher_reservations():
    reservations = []
    # Lecture du fichier CSV
    with open('data/reservations.csv', mode='r') as file:
        reader = csv.reader(file)
        # Parcourt chaque ligne du fichier
        for row in reader:
            reservations.append({
                'nom': row[0],
                'telephone': row[1],
                'date': row[2],
                'heure': row[3],
                'personnes': row[4]
            })
    # Affiche chaque réservation
    for reservation in reservations:
        print(f"Nom: {reservation['nom']}, Téléphone: {reservation['telephone']}, Date: {reservation['date']}, Heure: {reservation['heure']}, Personnes: {reservation['personnes']}")

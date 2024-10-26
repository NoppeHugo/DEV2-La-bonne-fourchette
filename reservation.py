import csv
from datetime import datetime

def ajouter_reservation(client_name, client_phone, reservation_date, reservation_time, number_of_people, table_id, status="Confirmed"):
    with open('data/reservations.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        reservation_id = int(datetime.now().timestamp())  # Génère un identifiant unique basé sur l'horodatage
        writer.writerow([reservation_id, client_name, client_phone, reservation_date, reservation_time, number_of_people, table_id, status])
        print(f"Réservation ajoutée pour {client_name}.")

""" 
Exemple d'utilisation
ajouter_reservation("Jean Dupont", "0487123456", "2024-10-28", "19:30", 2, 5)
"""


def afficher_reservations():
    try:
        with open('data/reservations.csv', mode='r') as file:
            reader = csv.reader(file)
            print("Liste des réservations :")
            print("ID | Nom | Téléphone | Date | Heure | Nombre de personnes | Statut")
            print("-" * 70)  # Ligne de séparation
            
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
                
    except FileNotFoundError:
        print("Le fichier des réservations n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'appel à la fonction
afficher_reservations()


import os
import csv

def initialize_csv(filename, headers):
    # Crée le fichier uniquement s'il n'existe pas déjà
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)  # Écrit les en-têtes
        print(f"{filename} initialisé avec les en-têtes : {headers}")

def initialiser_fichiers():
    headers_reservations = ['reservation_id', 'client_name', 'client_phone', 'reservation_date', 'reservation_time', 'number_of_people', 'table_id', 'status']
    headers_tables = ['table_id', 'capacity', 'status', 'location']
    headers_commandes = ['order_id', 'table_id', 'item', 'quantity', 'status', 'timestamp']
    
    # Appelle initialize_csv pour chaque fichier CSV
    initialize_csv('reservations.csv', headers_reservations)
    initialize_csv('tables.csv', headers_tables)
    initialize_csv('commandes.csv', headers_commandes)

# Exécute la fonction d'initialisation une seule fois
initialiser_fichiers()

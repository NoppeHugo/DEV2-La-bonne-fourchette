def ajouter_commande(table_id, item, quantity, status="Preparing"):
    with open('data/commandes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        order_id = int(datetime.now().timestamp())  # Génère un identifiant unique basé sur l'horodatage
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Date et heure de la commande
        writer.writerow([order_id, table_id, item, quantity, status, timestamp])
        print(f"Commande pour {item} ajoutée à la table {table_id}.")

# Exemple d'utilisation
ajouter_commande(5, "Coq au vin", 2)

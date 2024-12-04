import csv

# Ajouter une commande
def ajouter_commande(table_id, details_commande):
    statut = 'En préparation'
    with open('data/commandes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([table_id, details_commande, statut])

# Mettre à jour le statut de la commande
def maj_statut_commande(table_id, nouveau_statut):
    commandes = []
    with open('data/commandes.csv', mode='r') as file:
        commandes = [row for row in csv.reader(file)]
    
    for commande in commandes:
        if commande[0] == table_id:
            commande[2] = nouveau_statut

    with open('data/commandes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(commandes)

def afficher_commandes():
    commandes = []
    # Ouvre le fichier commandes.csv en mode lecture
    with open('data/commandes.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        # Passe la première ligne (en-tête du fichier CSV)
        next(reader, None)
        # Lit chaque ligne et l'ajoute à la liste commandes
        for row in reader:
            commandes.append({
                'table_id': row[0],
                'plat': row[1],
                'quantite': row[2],
                'statut': row[3]
            })
    return commandes
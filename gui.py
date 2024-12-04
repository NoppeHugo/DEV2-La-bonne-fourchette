import tkinter as tk
import csv
from reservation import ajouter_reservation, modifier_reservation, annuler_reservation, afficher_reservations
from table import afficher_statut_tables, fusionner_tables
from commande import ajouter_commande, maj_statut_commande, afficher_commandes

def afficher_plan_salle():
    root = tk.Tk()
    root.title("Plan de Salle - La Bonne Fourchette")

    with open('data/tables.csv', mode='r') as file:
        tables = [row for row in csv.reader(file)]
    
    for idx, table in enumerate(tables):
        statut = table[1]
        color = 'green' if statut == 'libre' else 'red' if statut == 'occupée' else 'orange'
        tk.Button(root, text=f"Table {table[0]}", bg=color).grid(row=idx//5, column=idx%5)

def afficher_commandes_gui():
    commandes_window = tk.Toplevel()
    commandes_window.title("Commandes")
    commandes = afficher_commandes()
    for commande in commandes:
        label = tk.Label(commandes_window, text=str(commande))
        label.pack()

def afficher_reservations_gui():
    reservations_window = tk.Toplevel()
    reservations_window.title("Réservations")
    reservations = afficher_reservations()
    for reservation in reservations:
        label = tk.Label(reservations_window, text=str(reservation))
        label.pack()

root = tk.Tk()
root.title("La Bonne Fourchette - Gestion")

bouton_afficher_commandes = tk.Button(root, text="Afficher Commandes", command=afficher_commandes_gui)
bouton_afficher_commandes.pack()

bouton_afficher_reservations = tk.Button(root, text="Afficher Réservations", command=afficher_reservations_gui)
bouton_afficher_reservations.pack()

root.mainloop()

if __name__ == "__main__":
    afficher_plan_salle()

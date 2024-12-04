from gui import afficher_plan_salle, afficher_commandes_gui, afficher_reservations_gui
from reservation import ajouter_reservation, modifier_reservation, annuler_reservation
from table import afficher_statut_tables, fusionner_tables
from commande import ajouter_commande, maj_statut_commande
from backup import sauvegarde_manuelle

def main():
    # Exécution du plan de salle (interface graphique)
    afficher_plan_salle()
    afficher_commandes_gui()
    afficher_reservations_gui()

if __name__ == "__main__":
    main()

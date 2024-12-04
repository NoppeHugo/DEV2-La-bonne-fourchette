import shutil
import datetime

def sauvegarde_manuelle():
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copyfile('data/reservations.csv', f'data/backup/reservations_{date_str}.csv')
    shutil.copyfile('data/tables.csv', f'data/backup/tables_{date_str}.csv')
    shutil.copyfile('data/commandes.csv', f'data/backup/commandes_{date_str}.csv')
    print("Sauvegarde effectuée.")

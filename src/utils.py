import os
import datetime

# Fonction pour obtenir l'heure actuelle
def get_current_time():
    return datetime.datetime.now()

# Fonction pour s'assurer qu'un répertoire existe
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

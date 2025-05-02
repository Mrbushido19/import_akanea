import logging
import os
from datetime import datetime

def setup_logging():
    # Créer le dossier logs s'il n'existe pas
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Créer le nom du fichier de log avec la date actuelle
    log_filename = f'logs/akanea_import_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    
    # Configurer le logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()  # Pour afficher les logs dans la console aussi
        ]
    )
    
    return logging.getLogger(__name__) 
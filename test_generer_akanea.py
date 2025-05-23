import pyautogui
import keyboard as key
import os
from dotenv import load_dotenv
import time
from logging_config import setup_logging
import cv2
import numpy 

# Initialiser le logger
logger = setup_logging()

# Charger les variables d'environnement
load_dotenv()

def connect_to_remote_desktop():
    """Se connecte au bureau distant avec les informations stockées dans .env"""
    logger.info("Connexion au bureau distant...")
    try:
        pyautogui.moveTo(154,1058, duration=1)
        pyautogui.click()
        pyautogui.write('Connexion ', interval=0.1)
        pyautogui.press('enter')

        pyautogui.moveTo(910, 324, duration=1)
        pyautogui.click()
        pyautogui.hotkey('ctrl', "A")
        pyautogui.press("delete")

        pyautogui.write(os.getenv('IP_ADDRESS'), interval=0.1)
        pyautogui.press('enter')
        time.sleep(5)
        key.write(os.getenv('PASSWORD'))
        pyautogui.press('enter')
        pyautogui.moveTo(1013, 497, duration=1)
        pyautogui.click()
        time.sleep(10)

        logger.info("Connexion au bureau distant réussie.")
    except Exception as e:
        logger.error(f"Erreur lors de la connexion au bureau distant : {e}")

def wait_for_image(image_path, timeout=60):
    """Attend que l'image soit détectée sur l'écran en utilisant OpenCV"""
    logger.info(f"Attente de l'image {image_path} pendant {timeout} secondes.")
    start_time = time.time()
    
    # Charger l'image template
    template = cv2.imread(image_path)
    if template is None:
        raise ValueError(f"Impossible de charger l'image {image_path}")
    
    while time.time() - start_time < timeout:
        try:
            # Prendre une capture d'écran
            screenshot = pyautogui.screenshot("img\\screenshot.png")
            screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)
            
            # Faire la correspondance de template
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            # Si la correspondance est suffisamment bonne (seuil de 0.8)
            if max_val >= 0.8:
                logger.info(f"Image trouvée avec une confiance de {max_val:.2f}")
                return True
                
        except Exception as e:
            logger.debug(f"Image non trouvée: {e}")
        time.sleep(1)
    return False

def open_akanea():
    """Ouvre l'application Akanea"""
    logger.info("Ouverture de l'application Akanea...")
    try:
        
        pyautogui.moveTo(74, 1061, duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.write("Akanea tms", interval=0.1)
        pyautogui.press("enter")
        pyautogui.moveTo(1034, 550, duration=1)
        time.sleep(2)
        pyautogui.click()
        time.sleep(5)
        pyautogui.click()
        time.sleep(20)
        logger.info("Application Akanea ouverte.")
    except Exception as e:
        logger.error(f"Erreur lors de l'ouverture d'Akanea : {e}")

def login_akanea():
    """Se connecte à Akanea"""
    logger.info("Connexion à Akanea...")
    try:
        pyautogui.moveTo(931, 539, duration=1)
        pyautogui.click()
        key.write(os.getenv('MDP_AKANEA'))
        pyautogui.moveTo(905, 649, duration=1)
        pyautogui.click()
        time.sleep(45)
        logger.info("Connexion à Akanea réussie.")
    except Exception as e:
        logger.error(f"Erreur lors de la connexion à Akanea : {e}")

def navigate_to_facturation():
    """Navigue vers la section facturation"""
    logger.info("Navigation vers la section facturation...")
    try:
        pyautogui.moveTo(49,166, duration=1)
        pyautogui.click()
        pyautogui.moveTo(90,214, duration=1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(175,35, duration=1)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(612,558, duration=1)
        pyautogui.click()
        time.sleep(30)
        logger.info("Navigation vers la facturation terminée.")
    except Exception as e:
        logger.error(f"Erreur lors de la navigation vers la facturation : {e}")

def generate_factures():
    """Génère les factures pour la période spécifiée"""
    logger.info("Génération des factures...")
    try:
        pyautogui.moveTo(138,118, duration=1)
        pyautogui.click()
        pyautogui.moveTo(622, 308, duration=1)
        pyautogui.click()
        
        for _ in range(10):
            pyautogui.press('backspace')
        key.write("01012025")
        
        pyautogui.moveTo(650, 366, duration=1)
        pyautogui.click()
        pyautogui.moveTo(569, 401, duration=1)
        pyautogui.click()
        pyautogui.moveTo(562, 477, duration=1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(927, 447, duration=1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(1162,606, duration=1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.screenshot("img\\facture_erreur.png", region=(0, 0, 1920, 1080))
        logger.info("Factures générées avec succès.")
    except Exception as e:
        logger.error(f"Erreur lors de la génération des factures : {e}")



def close_akanea():
    """
    Fermer Akanea """
    logger.info("Fermeture d'Akanea...")
    try:
       
        pyautogui.moveTo(1894,5, duration=1)
        pyautogui.doubleClick()
        
        pyautogui.moveTo(1074,606, duration=1)
        pyautogui.click()  
    except Exception as e:
        print(f"Erreur lors de la fermeture d'Akanea : {e}")

def main():
    """Fonction principale qui exécute toutes les étapes"""
    logger.info("Début du script d'automatisation Akanea.")
    

    connect_to_remote_desktop()
    while wait_for_image("C:\\Users\\acoulibaly\\Desktop\\import_akanea\\valid_img\\Bureau.PNG") == False :
        print("L'image n'a pas été détectée dans le délai imparti")
        return
    open_akanea()
    while wait_for_image("C:\\Users\\acoulibaly\\Desktop\\import_akanea\\valid_img\\AKANEA.PNG") == False :
        print("L'image n'a pas été détectée dans le délai imparti")
        return
   
    login_akanea()
    while wait_for_image("C:\\Users\\acoulibaly\\Desktop\\import_akanea\\valid_img\\FACTURATION.PNG") == False :
        print("L'image n'a pas été détectée dans le délai imparti")
        return
   
    navigate_to_facturation()
    # generate_factures()
    close_akanea()
    
    while wait_for_image("C:\\Users\\acoulibaly\\Desktop\\import_akanea\\valid_img\\Bureau.PNG") == False :
        print("L'image n'a pas été détectée dans le délai imparti")
        return

    logger.info("Script terminé.")

if __name__ == "__main__":
    main()
from datetime import datetime
from test_generer_akanea import logger
import pyautogui
import keyboard as key
import os
from dotenv import load_dotenv
import time
import pandas as pd
from logging_config import setup_logging
import subprocess

# Initialiser le logger
# logger = setup_logging()
def open_sage():
    """Ouvre le logiciel Sage"""
    logger.info("Ouverture de Sage...")
    pyautogui.moveTo(49,765, duration=1)
    pyautogui.doubleClick()
    time.sleep(2)

def connect_sage():
    """Se connecte à Sage avec les informations stockées dans .env"""
    logger.info("Connexion à Sage...")
    pyautogui.moveTo(936,479, duration=1)
    time.sleep(10)
    pyautogui.click()
    for _ in range(25):
        pyautogui.press('backspace')
    key.write(os.getenv('SAGE_USER'))
    pyautogui.press('tab')
    key.write(os.getenv('SAGE_PASSWORD'))
    pyautogui.press('enter')
    time.sleep(5)
    logger.info("Connexion à Sage réussie.")
    
def import_txt(txt_path):
    """Importe le fichier texte dans Sage"""
    logger.info(f"Importation du fichier {txt_path} dans Sage...")
    pyautogui.moveTo(29, 52, duration=1)
    pyautogui.click()
    pyautogui.moveTo(117,254, duration=1)
    time.sleep(2)
    pyautogui.moveTo(355,255, duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(302,410, duration=1)
    pyautogui.click()
    time.sleep(2)
    key.write(txt_path)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    logger.info("Importation réussie.")
    time.sleep(30)



def export_to_sage(ema_path, export_path):
    """Exportation vers Sage"""
    logger.info("Exportation vers Sage...")
    pyautogui.moveTo(29, 52, duration=1)
    pyautogui.click()
    pyautogui.moveTo(75,276, duration=1)
    time.sleep(2)
    pyautogui.moveTo(368,272, duration=1)
    pyautogui.moveTo(409,320, duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(385,482, duration=1)
    pyautogui.click()
    time.sleep(2)
    key.write(ema_path)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(573,438, duration=1)
    pyautogui.click()
    time.sleep(2)
    key.write(export_path)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(955,513, duration=1)
    pyautogui.click()
    time.sleep(2)
    for _ in range(10):
            pyautogui.press('backspace')
    key.write("150125")
    pyautogui.moveTo(1086,510, duration=1)
    pyautogui.click()
    time.sleep(2)
    for _ in range(10):
            pyautogui.press('backspace')
    key.write("150125")
    pyautogui.press('enter')
    time.sleep(5)
    logger.info("Exportation réussie.")
       
def main():
    """Fonction principale"""
    
    export_path = f"\\\\172.16.10.75\\rpa\\SAGE_X3\\export_sage100_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    # xls_path = f"\\\\172.16.10.75\\rpa\\SAGE_X3\\export_sage100_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    
    # df = pd.read_csv(export_path, delimiter=';')
    # df.to_excel(xls_path, index=False)
    # os.remove(export_path)
    time.sleep(5)
    # Charger les variables d'environnement
    load_dotenv()
    
    # Ouvrir Sage
    open_sage()
    
    # Se connecter à Sage
    connect_sage()
    
    # Importer le fichier texte
    txt_path = os.getenv('TXT_PATH')
    
    import_txt(txt_path)
    export_to_sage(os.getenv('EMA_PATH'), export_path=export_path)
    
if __name__ == "__main__":
    main()

import pyautogui
import keyboard as key
import os
from dotenv import load_dotenv
import time
from logging_config import setup_logging
import subprocess

# Initialiser le logger
logger = setup_logging()
def open_sage():
    """Ouvre le logiciel Sage"""
    logger.info("Ouverture de Sage...")
    pyautogui.moveTo(144,137, duration=1)
    pyautogui.doubleClick()
    time.sleep(2)

def connect_sage():
    """Se connecte à Sage avec les informations stockées dans .env"""
    logger.info("Connexion à Sage...")
    pyautogui.moveTo(936,479, duration=1)
    pyautogui.click()
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
    pyautogui.moveTo(375,436, duration=1)
    pyautogui.click()
    time.sleep(2)
    key.write(txt_path)
    pyautogui.press('enter')
    time.sleep(5)
    logger.info("Importation réussie.")
    
def main():

    
    # Charger les variables d'environnement
    load_dotenv()
    
    # Ouvrir Sage
    open_sage()
    
    # Se connecter à Sage
    connect_sage()
    
    # Importer le fichier texte
    txt_path = os.getenv('TXT_PATH')
    import_txt(txt_path)
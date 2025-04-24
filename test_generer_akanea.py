import pyautogui
import keyboard as key
import os
from dotenv import load_dotenv
import time

# Charger les variables d'environnement
load_dotenv()

def connect_to_remote_desktop():
    """Se connecte au bureau distant avec les informations stockées dans .env"""
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

def open_akanea():
    """Ouvre l'application Akanea"""
    pyautogui.moveTo(1013, 497, duration=1)
    pyautogui.click()
    time.sleep(10)

    pyautogui.moveTo(74, 1061, duration=1)
    pyautogui.click()
    pyautogui.write("Akanea tms", interval=0.1)
    pyautogui.press("enter")
    pyautogui.moveTo(1034, 550, duration=1)
    time.sleep(2)
    pyautogui.click()
    time.sleep(5)
    pyautogui.click()
    time.sleep(20)

def login_akanea():
    """Se connecte à Akanea"""
    pyautogui.moveTo(931, 539, duration=1)
    pyautogui.click()
    key.write(os.getenv('MDP_AKANEA'))
    pyautogui.moveTo(905, 649, duration=1)
    pyautogui.click()
    time.sleep(75)

def navigate_to_facturation():
    """Navigue vers la section facturation"""
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

def generate_factures():
    """Génère les factures pour la période spécifiée"""
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

def main():
    """Fonction principale qui exécute toutes les étapes"""
    connect_to_remote_desktop()
    open_akanea()
    login_akanea()
    navigate_to_facturation()
    # generate_factures()

if __name__ == "__main__":
    main()
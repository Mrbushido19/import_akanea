# Automatisation Akanea

Ce projet contient un script d'automatisation pour Akanea utilisant PyAutoGUI.

## Configuration de l'environnement

### Méthode 1 : Utilisation du script de configuration (Windows)
1. Double-cliquez sur `setup_env.bat`
2. Attendez que l'installation se termine

### Méthode 2 : Configuration manuelle
1. Créez un environnement virtuel :
```bash
python -m venv import_akanea
```

2. Activez l'environnement virtuel :
- Windows :
```bash
import_akanea\Scripts\activate
```
- Linux/Mac :
```bash
source import_akanea/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Configuration des variables d'environnement
1. Assurez-vous que le fichier `.env` existe à la racine du projet
2. Configurez les variables suivantes dans le fichier `.env` :
```
IP_ADDRESS=votre_adresse_ip
PASSWORD=votre_mot_de_passe
```

## Exécution du script
1. Activez l'environnement virtuel si ce n'est pas déjà fait :
```bash
import_akanea\Scripts\activate
```

2. Exécutez le script :
```bash
python pyAutoGui/test_generer_akanea.py
```

## Structure du projet
- `pyAutoGui/test_generer_akanea.py` : Script principal d'automatisation
- `.env` : Fichier de configuration des variables d'environnement
- `requirements.txt` : Liste des dépendances Python
- `setup_env.bat` : Script de configuration de l'environnement (Windows)
- `import_akanea/` : Dossier de l'environnement virtuel Python 
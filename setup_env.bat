@echo off
echo Creation de l'environnement virtuel import_akanea...
python -m venv import_akanea

echo Activation de l'environnement virtuel...
call import_akanea\Scripts\activate.bat

echo Installation des dependances...
pip install -r requirements.txt

echo Configuration terminee !
echo Pour activer l'environnement, utilisez: import_akanea\Scripts\activate.bat
pause 
@echo off
echo Démarrage de test_generer_akanea...
python test_generer_akanea.py
if %errorlevel% neq 0 (
    echo Erreur lors de l'exécution de test_generer_akanea
    pause
    exit /b %errorlevel%
)
echo Démarrage de import_sage...
python import_sage.py
if %errorlevel% neq 0 (
    echo Erreur lors de l'exécution de import_sage
    pause
    exit /b %errorlevel%
)
echo Toutes les commandes ont été exécutées avec succès
pause 
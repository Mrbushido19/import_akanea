@echo off
cls
echo ===============================
echo Démarrage du processus complet
echo ===============================

:: Étape 1 : test_generer_akanea.py
echo.
echo [1/2] Démarrage de test_generer_akanea.py...
python test_generer_akanea.py
if %errorlevel% neq 0 (
    echo [ERREUR] test_generer_akanea.py a échoué avec le code %errorlevel%
    pause
    exit /b 1
)

:: Étape 2 : import_sage.py
echo.
echo [2/2] Démarrage de import_sage.py...
python import_sage.py
if %errorlevel% neq 0 (
    echo [ERREUR] import_sage.py a échoué avec le code %errorlevel%
    pause
    exit /b 1
)

echo.
echo Toutes les commandes ont été exécutées avec succès.

:: Fermer automatiquement la fenêtre
exit /b 0

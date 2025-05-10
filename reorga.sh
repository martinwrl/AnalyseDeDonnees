#!/bin/bash

# Création des dossiers
mkdir -p TD1 TD2 TD3 TD4 TD5 TD6 data

# Déplacement des fichiers
mv scrabble.py motsSansAccent.txt frenchssaccent.dic TD1/
mv polynomes.py test_expression.py TD2/
mv arbres.py testsArbres.py testsArbres2.py TD3/
mv hashage.py TD4/
mv lignebrisee.py TD5/
mv entrelacsTD6.py TD6/
mv Infos.txt InfosCours.txt data/

# Suppression des fichiers inutiles
rm -f .DS_Store
rm -rf __pycache__/

# Ajout d'un fichier .gitignore pour ignorer les fichiers indésirables
echo ".DS_Store" >> .gitignore
echo "__pycache__/" >> .gitignore

# Git: commit et push
git add .
git commit -m "Réorganisation du projet : fichiers classés par TD"
git push
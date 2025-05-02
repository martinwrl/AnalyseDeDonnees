D'un point de vue global sur ton dépôt git, essaie d'organiser les séances par dossier pour que ca soit plus visible de voir et retrouver les différents TD.

Maintenant, ton fichier est plutôt propre et bien organisé, avec les questions à part, et quelques commentaires. La logique est plutôt bonne, à part pour la mise à jour d'une valeur: comme tu ajoutes toujours la clé sans vérifier si elle y est déjà, tu avoir plusieurs fois la même clé dans ta liste de collisions, avec des valeurs différentes, mais tu récupéreras toujours la première mise, donc pas de mise à jour. Tu dois vérifier si la clé n'est pas déjà dans la table de collisions avant de l'ajouter.

Voici le corrigé si tu veux regarder: https://github.com/thomas-vinet/Mines-TD-PSD
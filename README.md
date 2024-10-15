
# Tamagotchi

Ce projet vise à développer une application Python simulant plusieurs animaux virtuels 
(comme les Tamagotchi). Le joueur doit s'occuper de 5 animaux et les maintenir en 
bonne santé le plus longtemps possible. L'état de chaque animal est défini par plusieurs 
variables qui évoluent en fonction du temps et des actions du joueur. Nous avons utilisé 
la bibliothèque Pygame pour créer une interface graphique, rendant le jeu plus vivant et 
intuitif


## Spécifications Fonctionnelles
Fonctions Implémentées
1.Affichage de l'état des animaux : Le jeu affiche les états de faim, de 
santé, d'ennui et de fatigue de chaque animal.
2.Nourrir : Le joueur peut choisir un animal et le nourrir, augmentant ainsi 
son niveau de faim.
3.Jouer : Le joueur peut choisir un animal et jouer avec lui, augmentant son 
niveau d'ennui mais réduisant sa fatigue.
4. Sommeil : Les animaux peuvent entrer aléatoirement en état de sommeil, 
pendant lequel ils récupèrent de la santé, réduisent leur ennui et augmentent 
leur fatigue.
5.Temps de jeu : Le temps de jeu est calculé en jours, chaque jour durant 3 
minutes. Chaque jour, les stocks de nourriture et les états des animaux sont 
réinitialisés.
6.Fin du jeu : Si l'un des états (faim, santé ou fatigue) de n'importe quel 
animal tombe à zéro, le jeu se termine et la raison de l'échec est affichée.
7.Interface Graphique : Utilisation de Pygame pour créer une interface 
graphique incluant de la musique de fond, un écran de démarrage, des boutons 
interactifs et des effets de transition.
## Améliorations et Extensions
8.Interface graphique : En plus de l'interface de ligne de commande de 
base, nous avons développé une interface graphique Pygame, rendant le jeu plus 
intuitif et interactif.
9.Amélioration des règles du jeu : Nous avons ajusté les règles du jeu 
pour les rendre plus challengantes :
 1，Faim : Diminution de 8 points par seconde, plus rapide que la diminution 
de 5 points par seconde initialement prévue.
 2，Ennui : Diminution de 5 points par seconde, plus rapide que la 
diminution de 3 points par seconde initialement prévue.
 3，Fatigue : Augmentation de 1 point par seconde, rendant la gestion de la 
fatigue plus difficile.
 4，Impact de l'ennui sur la santé : Quand l'ennui atteint 0, tous les animaux 
perdent 8 points de santé par seconde, tandis que l'animal actuellement sélectionné 
perd 10 points de santé par seconde, renforçant l'impact de l'ennui sur la santé.
10. Bagarre entre animaux : Tous les animaux perdent 8 points de 
santé par seconde, tandis que l'animal actuellement sélectionné perd 10 points 
de santé par seconde, augmentant la difficulté du jeu.
11. Sons : Nous avons ajouté de la musique d'ambiance et des effets 
sonores de clic, améliorant l'immersion dans le jeu.
12. Écrans de démarrage et transitions : Nous avons implémenté 
des écrans de démarrage et des transitions en fondu, rendant le jeu plus 
attrayant.
13. Gestion de la fatigue : Nous avons introduit une gestion de la 
fatigue pour rendre le jeu plus challengeant et réaliste.
14. Images personnalisées pour les animaux : Les membres de 
l'équipe ont dessiné eux-mêmes toutes les images des animaux, y compris 
différentes images pour les états de veille et de sommeil. Ces images 
personnalisées rendent le jeu unique et vivant.
15. Gestion du code via GitHub : Nous avons utilisé GitHub pour la 
gestion du code et le contrôle de version. Chaque membre était responsable de 
différents modules et fonctionnalités, intégrés ensuite dans le programme 
principal
## Structures de Données
Dictionnaire des Données des Animaux :
o Nom (name)
o Images (images)
o Faim (hunger)
o Santé (health)
o Ennui (boredom)
o Fatigue (fatigue)
o État de sommeil (sleeping)
o Minuteur de sommeil (sleep_timer)
o Dernier temps de sommeil (last_sleep_time)
o Coordonnées (x, y)
o Vitesse (speed_x, speed_y)
17. Liste des Animaux :
o Contient 5 dictionnaires représentant les animaux.
18. Autres Données :
o État du jeu (running)
o Horloge du jeu (clock)
o Temps de jeu par jour (game_time)
o Nombre de jours passés (days_passed)
o Stock de nourriture (food_stock)
o Animal sélectionné (selected_pet)
o Indicateur de fin de jeu (game_over)
o Raison de la fin du jeu (game_over_reason)

## Répartition des Modules
Module Principal :
o main.py : Initialise le jeu, gère la boucle d'événements et met à jour 
l'interface.
20. Modules Fonctionnels :
o pet.py : Gère la création, la mise à jour et l'affichage des animaux.
o game.py : Gère la réinitialisation du jeu, l'écran de démarrage et les 
effets de transition.
## Gestion de Projet
Notre équipe a adopté une méthode de développement collaboratif en utilisant GitHub 
pour la gestion du code et le contrôle de version. Chaque membre était responsable de 
différents modules et fonctionnalités, intégrés ensuite dans le programme principal. 
Nous avons tenu des réunions en ligne régulières pour discuter de l'avancement du 
projet et des problèmes rencontrés, assurant ainsi la bonne progression du projet
## État du Projet et Couverture Fonctionnelle
Pendant le développement, nous avons implémenté toutes les fonctionnalités de base 
ainsi que plusieurs améliorations, y compris l'interface graphique, les effets sonores, 
l'écran de démarrage et les effets de transition. La seule fonctionnalité non implémentée 
est la sauvegarde et la restauration du jeu, que nous prévoyons d'ajouter dans les 
futures versions.
## Qualité du Code
Nommage des Variables et Fonctions : Tous les noms de 
variables et fonctions sont descriptifs, rendant le code plus lisible et maintenable.
22. Commentaires : Des commentaires détaillés ont été ajoutés aux 
sections clés pour faciliter la compréhension de la logique et des fonctionnalités 
du code.
23. Conception Modulaire : Le projet a été divisé en plusieurs 
modules, chacun responsable d'une fonctionnalité spécifique, améliorant la 
maintenabilité et l'évolutivité du code
## Tests et Résultats
Lors de la cinquième séance, nous avons intégré et testé le projet. Toutes les 
fonctionnalités principales ont été mises en œuvre et testées avec succès, y compris :
• Initialisation et mise à jour des états des animaux.
• Interactions du joueur avec les animaux (nourrir et jouer)
• Gestion du temps de jeu et des jours.
• Détection et gestion des conditions de fin de jeu.
• Affichage et interaction avec l'interface graphique.
La seule fonctionnalité non réalisée est la sauvegarde et la restauration du jeu, que nous 
prévoyons d’ajouter dans les futures améliorations
## Conclusion
Ce projet nous a permis de renforcer nos compétences en programmation Python et 
d'améliorer notre capacité à travailler en équipe. Nous avons appris à appliquer nos 
connaissances de programmation dans un projet réel, à communiquer et collaborer 
efficacement au sein de l'équipe, et à gérer notre temps et nos tâches pour atteindre les 
objectifs du projet. Nous sommes satisfaits du résultat final du projet et attendons avec 
impatience d'autres opportunités pour améliorer et étendre ce jeu
## Autheurs

- [@ArthurXian](https://www.github.com/ArthurXian)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


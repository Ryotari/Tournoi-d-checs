# Application gérant un tournoi d'échecs

### Openclassroom projet 04

Le projet consiste à créer une application permettant de créer et gérer des tournois d'échecs. Le programme utilise un algorithme permettant de calculer la rotation des joueurs afin que les matchs soit équitables et ne se reproduisent pas (algorithme suisse de tournois).

Le programme utilise le design pattern MVC (Modèles - Vues - Controlleurs), et utilise la librairie TinyDB pour sauvegarder les joueurs et les tournois dans une base de données.

Il permet de :

- Créer et sauvegarder des joueurs.
- Mettre à jour le classement d'un joueur.
- Créer des tournois
- Lancer des tournois.
- Sauvegarder et charger des tournois



## Prérequis

Vous devez installer python, la dernière version se trouve à cette adresse 
https://www.python.org/downloads/

Les scripts python se lancent depuis un terminal

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont repertoriés dans le fichier ```requirements.txt```

Vous pouvez installer un environnement externe via la commande 

```bash
pip install venv
```
dans le terminal, puis le lancer avec la commande (Pour Windows Powershell):

```bash
env/Scripts/activate.ps1
```

Ensuite, entrez la commande :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.



## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et repertoires du repository, et lancer le programme depuis un terminal via la commande :

```bash
python main.py
```

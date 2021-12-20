from models import player_model

class PlayerDisplay:

    def __call__(self):
        """player_db = player_model.player_db"""

        for player in player_list:
            print(f"{player['Nom']} {player['Prénom']} {player['Classement']}")


class PlayerMenus:

    player_menu = [('1', 'Créer un joueur'),
                   ('2', 'Modifier un joueur existant'),
                   ('3', 'Retour au menu')]

    player_search_menu = [('1', 'Chercher par ordre alphabétique'),
                          ('2', 'Chercher par classement'),
                          ('3', 'Retour au menu')]
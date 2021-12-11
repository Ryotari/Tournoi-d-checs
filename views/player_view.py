from models import player_model

class PlayerDisplay:

    def __call__(self):
        """player_db = player_model.player_db"""

        for player in player_list:
            print(f"{player['Nom']} {player['Prénom']} {player['Classement']}")
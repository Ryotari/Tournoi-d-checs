from tinydb import TinyDB


player_database = TinyDB('models/players.json')


class Player:
    """Create an instance of a player"""
    def __init__(self, player_controller):
        self.controller = player_controller

    def serialized_player(self, player):
        player_data = {
            'last_name': player['last_name'],
            'first_name': player['first_name'],
            'birthdate': player['birthdate'],
            'gender': player['gender'],
            'ranking': player['ranking'],
            'player_id': player['player_id']
        }

        return player_data

    def unserialized_player(self, serialized_player):
        last_name = serialized_player['last_name']
        first_name = serialized_player['first_name']
        birthdate = serialized_player['birthdate']
        gender = serialized_player['gender']
        ranking = serialized_player['ranking']
        player_id = serialized_player['player_id']

        return Player(last_name,
                      first_name,
                      birthdate,
                      gender,
                      ranking,
                      player_id
                      )

    def add_player_id(self):
        player_id = len(player_database) + 1

        return player_id

    def add_player_to_database(self, player):
        player_database.insert(player)

    def save_player(self, data):
        player = self.serialized_player(data)
        self.add_player_to_database(player)
        print('Le joueur a été ajouté à la base de données.\n')

    def send_player_database(self):

        return player_database

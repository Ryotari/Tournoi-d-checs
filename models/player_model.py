#from tinydb import TinyDB


#players_db= TinyDB('player_db.json')


class Player:
    """Create an instance of a player"""
    
    def __init__(self):
        self.PLAYERS_LIST = []

    def __repr__(self):
        return f'{self.last_name} {self.first_name}, classement : {self.ranking}'

    def serialized_player(self, player):
        player_data = {
            'last_name': player['last_name'],
            'first_name': player['first_name'],
            'birthdate': player['birthdate'],
            'gender': player['gender'],
            'ranking': player['ranking'],
            'score': player['score'],
            'player_id': player['player_id']
        }

        return player_data


    def unserialized_player(self, serialized_player):
        last_name = serialized_player['last_name']
        first_name = serialized_player['first_name']
        birthdate = serialized_player['birthdate']
        gender = serialized_player['gender']
        ranking = serialized_player['ranking']
        score = serialized_player['score']
        player_id = serialized_player['player_id']
        
        return Player(last_name,
                      first_name, 
                      birthdate,
                      gender,
                      ranking,
                      score,
                      player_id
                      )

    def add_player_id(self):
        player_id = len(self.PLAYERS_LIST) + 1

        return player_id
        
    def add_player_to_database(self, player):
        self.PLAYERS_LIST.append(player)

    def save_player(self, data):
        player = self.serialized_player(data)
        self.add_player_to_database(player)
        print(self.PLAYERS_LIST)

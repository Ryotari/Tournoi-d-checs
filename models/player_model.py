from tinydb import TinyDB


#players_db= TinyDB('player_db.json')

player_list = []

class Player:
    """Create an instance of a player"""
    
    def __init__(self, 
                last_name=None, 
                first_name=None, 
                birthdate=None, 
                gender=None,
                ranking=None,
                score=0,
                player_id=0
                ):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.payer_id = player_id


    def __repr__(self):
        return f'{self.last_name} {self.first_name}, classement : {self.ranking}'


    def serialized_player(self):
        player_informations = {}
        player_informations['Nom'] = self.last_name
        player_informations['Prénom'] = self.first_name
        player_informations['Date de naissance'] = self.birthdate
        player_informations['Sexe'] = self.gender
        player_informations['Classement'] = self.ranking
        player_informations['Score'] = self.score
        player_informations['ID du joueur'] = self.player_id

        return player_informations


    def unserialized_player(self, serialized_player):
        last_name = serialized_player(last_name)
        first_name = serialized_player(first_name)
        birthdate = serialized_player(birthdate)
        gender = serialized_player(gender)
        ranking = serialized_player(ranking)
        score = serialized_player(score)
        player_id = serialized_player(player_id)
        return Player(last_name,
                      first_name, 
                      birthdate,
                      gender,
                      ranking,
                      score,
                      player_id
                      )


    def add_to_database(self):
        player = Player(player_values[0],
                        player_values[1],
                        player_values[2],
                        player_values[3],
                        player_values[4]
                        )
        player_list.append(player)
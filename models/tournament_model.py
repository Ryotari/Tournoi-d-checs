from tinydb import TinyDB


tournament_database = TinyDB('models/tournament.json')


class Tournament:
    """Create an instance of a tournament"""

    def __init__(self, tournament_controller):
        self.controller = tournament_controller


    def serialized_tournament(self, tournament):
        tournament_data = {
            'tournament_name': tournament['tournament_name'],
            'location': tournament['location'],
            'date': tournament['date'],
            'number_of_tours': tournament['number_of_tours'],
            'time_control': tournament['time_control'],
            'description': tournament['description'],
            'tournament_id': tournament['tournament_id'],
            'players_ids': tournament['players_ids'],
            'player_scores': tournament['player_scores'],
            'list_of_tours': tournament['list_of_tours']
        }

        return tournament_data

    def unserialized_tournament(self, serialized_tournament):
        tournament_data = {
            'tournament_name': serialized_tournament['tournament_name'],
            'location': serialized_tournament['location'],
            'date': serialized_tournament['date'],
            'number_of_tours': serialized_tournament['number_of_tours'],
            'time_control': serialized_tournament['time_control'],
            'description': serialized_tournament['description'],
            'tournament_id': serialized_tournament['tournament_id'],
            'players_ids': serialized_tournament['players_ids'],
            'player_scores': serialized_tournament['player_scores'],
            'list_of_tours': serialized_tournament['list_of_tours']
        }
        return tournament_data



    def add_tournament_id(self):
        tournament_id = len(tournament_database) + 1

        return tournament_id

    def add_tournament_to_database(self, tournament):
        tournament_database.insert(tournament)

    def update_tournament(self, tournament):
        tournament_database.update({'list_of_tours': tournament['list_of_tours']}, doc_ids=[tournament['tournament_id']])
        tournament_database.update({'player_scores': tournament['player_scores']}, doc_ids=[tournament['tournament_id']])

    def save_tournament(self, data):
        """Save the tournament and add it to the database"""
        tournament = self.serialized_tournament(data)
        self.add_tournament_to_database(tournament)
        print('Le tournoi a été ajouté à la base de données.\n')

    def send_tournament_database(self):
        
        return tournament_database

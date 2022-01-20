"""from tinydb import TinyDB


tournament_database = TinyDB('tournament_db.json')"""


class Tournament:
    """Create an instance of a tournament"""

    def __init__(self, tournament_controller):
        self.controller = tournament_controller
        self.TOURNAMENTS_LIST = []

    def __repr__(self):
        return f"{self.tournament_name} - {self.location}\n"

    def serialized_tournament(self, tournament):
        tournament_data = {
            'tournament_name': tournament['tournament_name'],
            'location': tournament['location'],
            'date': tournament['date'],
            'number_of_tours': tournament['number_of_tours'],
            'time_control': tournament['time_control'],
            'description': tournament['description'],
            'tournament_id': tournament['tournament_id'],
            'players_entry': tournament['players_entry']
        }

        return tournament_data

    def unserialized_tournament(self, serialized_tournament):
        tournament_name = serialized_tournament['tournament_name']
        location = serialized_tournament['location']
        date = serialized_tournament['date']
        number_of_tours = serialized_tournament['number_of_tours']
        time_control = serialized_tournament['time_control']
        description = serialized_tournament['description']
        tournament_id = serialized_tournament['tournament_id']
        players_entry = serialized_tournament['players_entry']

        return Tournament(tournament_name,
                          location,
                          date,
                          number_of_tours,
                          time_control,
                          description,
                          tournament_id,
                          players_entry
                          )

    def add_tournament_id(self):
        tournament_id = len(self.TOURNAMENTS_LIST) + 1

        return tournament_id

    def add_tournament_to_database(self, tournament):
        self.TOURNAMENTS_LIST.append(tournament)


    def save_tournament(self, data):
        """Save the tournament and add it to the database"""
        tournament = self.serialized_tournament(data)
        self.add_tournament_to_database(tournament)
        print(self.TOURNAMENTS_LIST)

    def send_tournaments_list(self):
        TOURNAMENTS_LIST = self.TOURNAMENTS_LIST
        
        return TOURNAMENTS_LIST

from tinydb import TinyDB


tournament_database = TinyDB('tournament_db.json')


class Tournament:
    """Create an instance of a tournament"""

    def __init__(self, tournament_name=None,
                 location=None,
                 tournament_date=None,
                 number_of_tours=4,
                 time_control=None,
                 description=None,
                 list_of_tours=[],
                 ):

        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date = tournament_date
        self.number_of_tours = number_of_tours
        self.time_control = time_control
        self.description = description
        self.list_of_tours = list_of_tours

    def __repr__(self):
        return f"{self.tournament_name} - {self.location}\n"

    def serialized_tournament(self):
        tournament_informations = {}
        tournament_informations['Nom du tournoi'] = self.tournament_name
        tournament_informations['Lieu'] = self.location
        tournament_informations['Date'] = self.tournament_date
        tournament_informations['Nombre de tours'] = self.number_of_tours
        tournament_informations['Controle du temps'] = self.time_control
        tournament_informations['Description'] = self.description
        tournament_informations["Tours"] = self.list_of_tours

        return tournament_informations

    def unserialized_tournament(self, serialized_tournament):
        tournament_name = serialized_tournament['Nom du tournoi']
        location = serialized_tournament['Lieu']
        tournament_date = serialized_tournament['Date']
        number_of_tours = serialized_tournament['Nombre de tours']
        time_control = serialized_tournament['Controle du temps']
        description = serialized_tournament['Description']
        list_of_tours = serialized_tournament["Tours"]


        return Tournament(tournament_name,
                          location,
                          tournament_date,
                          number_of_tours,
                          time_control,
                          description,
                          list_of_tours,
                          )

    def add_to_database(self, tournament_values):
        tournament = Tournament(tournament_values[0],
                                tournament_values[1],
                                tournament_values[2],
                                tournament_values[3],
                                tournament_values[4],
                                tournament_values[5]
                                )
from models import player_model
from views import player_view

class CreatePlayer:
    """Enter the player's informations and add him into the database"""
    def __init__(self):
        self.player_values = []
        self.player_keys = ['Nom', 
        					'Prénom', 
        					'Date de naissance', 
        					'Sexe', 
        					'Classement'
        					]

    def __call__(self):
        self.player_model = player_model.Player()
        self.player_values.append(self.add_last_name())
        self.player_values.append(self.add_first_name())
        self.player_values.append(self.add_birthdate())
        self.player_values.append(self.add_gender())
        self.player_values.append(self.add_ranking())
        self.player_model.add_to_db(self.player_values)


    def add_last_name(self):
        last_name = input('Nom de famille : ')
        while last_name == '':
            last_name = input('Entrez un nom de famille : ')
        return last_name

    def add_first_name(self):
        first_name = input('Nom de famille : ')
        while first_name == '':
            first_name = input('Entrez un nom de famille : ')
        return first_name

    def add_birthdate(self):
        birth_day = input('Entrez un jour de naissance : ')
        while(True):
            if birth_day.isdigit() \
            and len(birth_day) == 2 \
            and int(birth_day) <= 31:
                break
            else:
                birth_day = input('Jour invalide. '
                                  'Entrez un jour de naissance : ')

        birth_month = input('Entrez un mois de naissance : ')
        while(True):
            if birth_month.isdigit() \
            and len(birth_month) == 2 \
            and int(birth_month) <= 12:
                break
            else:
                birth_month = input('Mois invalide. '
                                    'Entrez un mois de naissance en chiffres : ')

        birth_year = input('Entrez une année de naissance : ')
        while(True):
            if birth_year.isdigit() \
            and len(birth_year) == 4 \
            and int(birth_year) <= 2020:
                break
            else:
                birth_year = input('Année invlide. '
                                   'Entrez une année de naissance : ')

        return f'{birth_day}/{birth_month}/{birth_year}'

    def add_gender(self):
        gender = input('Choisissez le sexe du joueur (H ou F) : ')
        while(True):
            if gender == 'H':
                return 'Homme'
            elif gender == 'F':
                return 'Femme'
            else:
                gender = input('Sexe invalide. '
                               'Choisissez le sexe du joueur (H ou F) : ')

    def add_ranking(self):
        ranking = input('Entrez le classement du joueur : ')
        while(True):
            if ranking.isdigit() and int(ranking) >= 0:
                return ranking
            else:
                ranking = input('Classement invalide. '
                                'Entrez le classement du joueur : ')


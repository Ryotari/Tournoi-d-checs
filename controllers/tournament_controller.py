from models import tournament_model
from views import tournament_view

class CreateTournament:
    """Enter the tournament's informations and add him into the database"""
    def __init__(self):
        self.tournament_values = []
        self.tournament_keys = ['Nom',
                                'Lieu',
                                'Date',
                                'Nombre de tours',
                                'Controle du temps',
                                'Description'
                                ]
        self.players_entry = []

    def __call__(self):
        self.tournament_values.append(self.add_tournament_name())
        self.tournament_values.append(self.add_location())
        self.tournament_values.append(self.add_tournament_date())
        self.tournament_values.append(self.add_number_of_rounds())
        self.tournament_values.append(self.add_time_control())
        self.tournament_values.append(self.add_description())
        self.tournament_model.add_to_db(self.tournament_values)


    def add_tournament_name(self):
        tournament_name = input('Nom du tournoi : ')
        while tournament_name == '':
            tournament_name = input('Nom invalide. '
                                    'Entrez le nom du tournoi : ')
        return tournament_name

    def add_location(self):
        tournament_location = input('Lieu du tournoi : ')
        while tournament_location == '':
            tournament_location = input('Lieu invalide. '
                                        'Entrez le lieu du tournoi : ')

    def add_tournament_date(self):
        tournament_day = input('Entrez le jour du tournoi : ')
        while(True):
            if tournament_day.isdigit() \
            and len(tournament_day) == 2 \
            and int(tournament_day) <= 31:
                break
            else:
                tournament_day = input('Jour invalide. '
                                       'Entrez le jour du tournoi : ')

        tournament_month = input('Entrez le mois du tournoi : ')
        while(True):
            if tournament_month.isdigit() \
            and len(tournament_month) == 2 \
            and int(tournament_month) <= 12:
                break
            else:
                tournament_month = input('Mois invalide. '
                                         'Entrez le mois du tournoi en chiffres : ')

        tournament_year = input('Entrez l\'année du tournoi : ')
        while(True):
            if tournament_year.isdigit() \
            and len(tournament_year) == 4 \
            and int(tournament_year) >= 2021:
                break
            else:
                tournament_year = input('Année invlide. '
                                        'Entrez l\'année du tournoi : ')

        return f'{tournament_day}/{tournament_month}/{tournament_year}'

    def add_number_of_rounds(self):
        number_of_rounds = 4
        print('Le nombre de tours par défaut est de 4. \n'
              'Souhaitez vous changer ce nombre ?')

        valid_rounds_number = False
        while not valid_rounds_number:
            round_choice = input("Entrez 'Y' pour changer, ou 'N' pour garder 4 : ")
            if round_choice == 'Y':
                number_of_rounds = input('Entrez le nombre de tours : ')
                if number_of_rounds.isdigit():
                    valid_rounds_number = True
                else:
                    print('Nombre de tours invalide. '
                          'Entrez le nombre de tours : ')
            if round_choice == 'N':
                valid_rounds_number = True
        return number_of_rounds

    def add_time_control(self):
        print('Choisissez le contrôle du temps. '
              'Entrez 1 pour le Bullet \n'
              'Entrez 2 pour le Blitz \n'
              'Entrez 3 pour le Coup Rapide')

        valid_time_control = False
        while not valid_time_control:
            time_control = input('Entrez votre choix : ')
            if time_control == '1':
                time_control = 'Bullet'
                valid_time_control = True
            if time_control == '2':
                time_control = 'Blitz'
                valid_time_control = True
            if time_control == '3':
                time_control = 'Coup Rapide'
                valid_time_control = True
            else:
                print('Choix invalide')
        return time_control

    def add_description(self):
        description = input('Entrez une description du tournoi : \n')
        return description
